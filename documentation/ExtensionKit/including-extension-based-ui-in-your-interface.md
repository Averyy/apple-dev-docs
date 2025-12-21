# Including extension-based UI in your interface

**Framework**: ExtensionKit

Build app extensions that provide a custom UI, and host those views in your app’s interface.

#### Overview

When adding support for app extensions, you can configure one of your app’s extension points to support a custom UI. You might choose this option when the app extension needs to manage the presented content. For example, an image-editing app might let app extensions present their own UI to configure custom image modifications.

To support app extensions with custom UI, both the app and app extensions must adopt the [`ExtensionKit`](ExtensionKit.md) framework. To display the app extension’s UI, the host app presents a view controller from its interface. The app extension provides the content for that view controller, delivering it the host app with the framework’s help.

##### Add the User Interface Attribute to Your Extension Point

To display custom UI from app extensions, the host app’s extension point must include the [`AppExtensionPoint.UserInterface`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/UserInterface) attribute in its extension point definition. When this attribute is present and has a value of `true`, the host app can incorporate custom UI from its app extensions. The following example shows an extension point definition that includes this attribute:

```swift
extension AppExtensionPoint {

    @Definition
    public static var greetingExtension: AppExtensionPoint {
        Name("GreetingUI")
        UserInterface(true)
        Scope(restriction: .none)
    }
}
```

In an app extension, the binding declaration you create remains the same whether or not you’re providing custom UI. You’re expected to know whether the extension point requires a custom UI. If you’re creating an app extension for another app, the app’s SDK needs to specify this information.

##### Display a Host View Controller From Your Apps Interface

You’re responsible for deciding how best to integrate UI from app extensions into your host app. You might incorporate this content in a separate window, as part of an inspector, in a settings panel, or in other ways.

To display the UI for an app extension, add an [`EXHostViewController`](exhostviewcontroller.md) to your app’s interface.
App extensions can provide multiple scenes of content, but the host view controller displays only one of those scenes at a time. When configuring the view controller, specify the identity of the app extension and a string with the name of the scene you want to display in the view controller’s [`configuration`](exhostviewcontroller/configuration-swift.property.md) property. The app extension uses the scene name to deliver the correct set of views to your app. To display a different scene, change the configuration details or display a new host view controller.

When building your interface with SwiftUI, wrap the [`EXHostViewController`](exhostviewcontroller.md) in a representable type for the corresponding platform. The [`UIViewControllerRepresentable`](https://developer.apple.com/documentation/SwiftUI/UIViewControllerRepresentable) and [`NSViewControllerRepresentable`](https://developer.apple.com/documentation/SwiftUI/NSViewControllerRepresentable) protocols give you a way to create a SwiftUI view using content from a UIKit or AppKit view controller. The following example shows a SwiftUI view for macOS that wraps the [`EXHostViewController`](exhostviewcontroller.md) type. The view stores the scene name and app extension identity as local variables, which it uses to configure the view controller.

```swift
struct ExtensionView: NSViewControllerRepresentable {
    typealias NSViewControllerType = EXHostViewController
    
    let identity: AppExtensionIdentity
    let sceneID: String
    
    func makeNSViewController(context: Context) -> EXHostViewController {
        let viewController = EXHostViewController()
        viewController.configuration = EXHostViewController.Configuration(appExtension: identity, sceneID: sceneID)
        
        return viewController
    }
    
    func updateNSViewController(_ uiViewController: EXHostViewController, context: Context) {
        uiViewController.configuration = EXHostViewController.Configuration(appExtension: identity, sceneID: sceneID)
    }
}
```

When you display an [`EXHostViewController`](exhostviewcontroller.md) in your app’s interface, either directly or as part of a SwiftUI view, the view controller loads the relevant views from the app extension. Treat the view controller’s content as opaque, and focus on where in your UI you want to display it. The following example displays the UI from one or more app extensions using the custom `ExtensionView` type from the previous example. The custom `viewModel` object locates the available app extensions using an [`AppExtensionPoint.Monitor`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Monitor) type.

```swift
struct ContentView: View {
    
    @State private var viewModel = ViewModel()

    var body: some View {
        NavigationStack {
        
            VStack {
                if viewModel.identities.count > 0 {
                    ForEach(viewModel.identities, id: \.self) { identity in
                        ExtensionView(identity: identity, sceneID: "GreetingScene")
                    }
                }
                else {
                    Text("No greeting available.")
                }
            }
            .padding()
            .task {
                await viewModel.load()
            }
        }
    }
}
```

For information about how to get the list of app extension identities using a monitor, see [`Discovering app extensions from your app`](https://developer.apple.com/documentation/ExtensionFoundation/discovering-app-extensions-from-your-app).

##### Create the Initial Scene for Your App Extension

To build an app extension with custom UI, create that UI using a special set of types from the [`ExtensionKit`](ExtensionKit.md) framework. The recommended way to create your custom views is with SwiftUI, and the framework provides SwiftUI scenes to incorporate into your app extension. When creating new app extensions, the Xcode templates provide the initial views you need to build your UI.

To create a new UI-based app extension:

1. Add a new target to your Xcode project.
2. Choose the Generic extension template.
3. Click Next.
4. In the options panel, set the extension type UI Extension.
5. Provide a name and specify other options for your app extension.
6. Click Finish.

The template code contains an initial code for you to modify. When starting from this template, make most of your changes in the custom [`AppExtension`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension) type:

- Put your SwiftUI views in the closure for the scene in the `body` property.
- Update the information in the [`AppExtensionPoint.Bind`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Bind). Specify the name of the host app and the specific extension point you’re supporting.
- Add any custom initialization code to the `init()` method.

The template’s `ExampleScene` type provides a concrete implementation of a scene that you can use without modification. This scene delivers your SwiftUI views to the host app using a [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) structure. To display the correct scene, make sure the string you passed to the initializer of this structure matches the scene the host app requests. In the example code, specify the scene name using the `sceneID` property, as shown in the following example:

```swift
struct ExampleScene<Content: View>: ExampleAppExtensionScene {
    
    let sceneID = "GreetingScene"

    public init(content: @escaping () ->  Content) {
        self.content = content
    }
    
    private let content: () -> Content
    
    public var body: some AppExtensionScene {
        PrimitiveAppExtensionScene(id: sceneID) {
            content()
        } onConnection: { connection in
            // TODO: Configure the XPC connection and return true
            return true
        }
    }
}
```

If your app extension offers multiple scenes, create a separate [`AppExtensionScene`](appextensionscene.md) type for each unique scene you display. If you’re starting from the Xcode template, duplicate the `ExampleScene` type and update the type name and scene ID information. To make each new scene type available, update the `body` property of the [`AppExtension`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension) subclass, as shown in the example below. When the host app requests a scene, [`ExtensionKit`](ExtensionKit.md) determines which scene contains a [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) with the matching scene ID and returns its content.

```swift
@main
class MyExtension : ExampleExtension {
   // The initializer and binding declaration code.

    var body: some ExampleAppExtensionScene {
        ExampleScene {
            Text("Scene 1!")
        }
        SecondScene {
            Text("Scene 2!")
        }
    }
}
```

##### Handle Incoming Xpc Connection Requests

[`ExtensionKit`](ExtensionKit.md) handles interface-related updates between the app extension and host app, but the host app might still want to exchange data directly with the app extension. For example, a host app might need to send data to the app extension that’s unrelated to the UI. To facilitate this type of transfer, the host app has two options:

- Configure an XPC connection that’s tied to a specific instance of the app extension’s UI.
- Configure an XPC connection that’s global to the app extension.

To communicate with a specific instance of the app extension’s UI, the host app makes an XPC connection using its [`EXHostViewController`](exhostviewcontroller.md) object. Calling the [`makeXPCConnection()`](exhostviewcontroller/makexpcconnection().md) method creates a connection to the [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) type in the app extension. Use the `onConnection` handler of that type to accept the XPC connection request and provide the host app with a proxy object, as shown in the following code:

```swift
public var body: some AppExtensionScene {
    PrimitiveAppExtensionScene(id: sceneID) {
        content()
    } onConnection: { connection in
        connection.exportedObject = MySceneManager
        connection.exportedInterface = NSXPCInterface(with: HostInterface.self)
        connection.resume()
        return true
    }
}
```

To create a global connection that’s independent of a specific UI instance, the host app initiates the XPC connection from its [`AppExtensionProcess`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionProcess) type. The app extension responds to connection requests using the [`accept(connection:)`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration/accept(connection:)) method in its [`AppExtensionConfiguration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration) type. For information about setting up this connection, see [`Building an app extension to support a host app`](https://developer.apple.com/documentation/ExtensionFoundation/building-an-app-extension-to-support-a-host-app#Configure-the-XPC-connection-to-the-host-app).

##### Respond to Activation and Deactivation Events

Creating and presenting an [`EXHostViewController`](exhostviewcontroller.md) from your app doesn’t guarantee the appearance of an app extension’s UI. [`ExtensionKit`](ExtensionKit.md) might need to launch the app extension and get it running first, before the host app tries to create an XPC connection to it. Similarly, the app extension might exit unexpectedly or require the dismantling of its views for other reasons. The host view controller reports these changes to its associated delegate object.

When the app extension is ready to accept an XPC connection, the host view controller calls its delegate’s [`hostViewControllerDidActivate(_:)`](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md) method. Use this method to initiate the XPC connection and start communication with the app extension. Similarly, use the delegate’s [`hostViewControllerWillDeactivate(_:error:)`](exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:).md) to close out the current connection and stop communicating with the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/including-extension-based-ui-in-your-interface)*