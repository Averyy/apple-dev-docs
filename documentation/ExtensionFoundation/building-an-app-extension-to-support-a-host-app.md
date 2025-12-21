# Building an app extension to support a host app

**Framework**: ExtensionFoundation

Create an app extension to perform tasks in a separate process from a host app.

#### Overview

An app extension extends the features of the host app it supports, and runs code in a separate process. You can develop an app extension together with your app, or develop app extensions separately to support a different app. The host app provides the interface your app extension must implement, and both the app and app extension adopt the [`ExtensionFoundation`](ExtensionFoundation.md) framework to manage interactions.

In an app extension, the [`ExtensionFoundation`](ExtensionFoundation.md) framework provides the code for running the main event loop and accepting XPC connections. When you create an app extension in Xcode, the generic extension template provides most of the code you need to get started. With that template, you add code to establish communications with the host app, and to implement the expected features.

> **Note**: The host app provides the SDK that you adopt when implementing your app extension. This SDK includes any API to adopt, the version of XPC to use, and any other requirements for the host app’s extension points.

##### Create Your App Extension Target

An app extension is a bundle that ships inside an existing app, so you must already have an Xcode project with an app before adding an app extension to it. When writing app extensions for one of your apps, or for another app on the App Store, start your app extension from the Generic Extension target type. The following steps walk you through the process of adding this target type to your existing Xcode project:

1. Open your Xcode project.
2. Select File > New > Target.
3. Choose the appropriate platform.
4. In the app extension section of the panel, select Generic Extension.
5. Click Next.
6. Provide a name for the extension.
7. Set the extension type to Non-UI Extension.
8. Select your app from the Embed in Application field.
9. Click Finish to create the target.

The Generic Extension target template provides the initial code your app extension needs to run. Specifically, it contains a customization of the [`AppExtension`](appextension.md) type that is the entry point for your app extension’s code. You don’t override this type’s existing behavior, but you do augment it with details about your app extension. For example, you provide it with an [`AppExtensionConfiguration`](appextensionconfiguration.md) object, which creates the XPC connection between your app extension and the host app.

##### Bind Your App Extension to an Appropriate Extension Point

Each time you create an app extension, you target one of the extension points of the associated host app. Extension points are features or capabilities for which the host app supports app extensions. For example, an image-editing app might define an extension point to support custom image filters. In your app extension code, you programmatically specify the extension point you support using a binding. At runtime, the system uses your binding information to match your app extension to the host app on a person’s device.

To create a binding in your app extension code, add a variable with the [`AppExtensionPoint`](appextensionpoint.md) type to your existing [`AppExtension`](appextension.md) structure. Set the contents of this variable to a closure with an [`AppExtensionPoint.Identifier`](appextensionpoint/identifier.md) type, which specifies the name of the extension point and the host app’s bundle identifier. Precede the definition of this variable with the [`AppExtensionPoint.Bind`](appextensionpoint/bind.md) property wrapper to tell the compiler that this variable contains your binding details. The following example shows a binding to an app with the extension point name `HostAppFeature`:

```swift
struct MyAppExtension: AppExtension {
    @AppExtensionPoint.Bind
    var boundAppExtensionPoint: AppExtensionPoint { 
        AppExtensionPoint.Identifier("com.example.hostapp", name "HostAppFeature")
    }
}
```

At build time, you use the compiler to generate the actual binding information the system needs. Add a user-defined build setting to your app extension target in Xcode, and set its name to `EX_ENABLE_EXTENSION_POINT_GENERATION` and its value to `YES`. When this setting is present, the compiler extracts the details from your binding code and puts the relevant details in your app extension’s information property list. When someone installs the app containing your app extension, the system reads the keys from this property list and uses them to match your app extension to its host app.

> **Note**: When creating new app extensions, always place binding information in your code. If you have an older app extension, the system still recognizes keys you added manually to your app’s information property list.

##### Configure the Xpc Connection to the Host App

Apart from adopting the host app’s required API, an app extension’s only requirement is to establish a communications channel with that app. After launching an app extension, the host app is responsible for initiating an XPC connection to that extension. Accept this connection in your app extension code to start communication with the host.

To accept an incoming XPC connection request, create a custom type that adopts the [`AppExtensionConfiguration`](appextensionconfiguration.md) protocol and initialize your [`AppExtension`](appextension.md) type with it. When the host app initiates an XPC connection, the system redirects the request to the code you provide in this type. Use that code to configure the XPC connection details and call the connection’s [`resume()`](https://developer.apple.com/documentation/Foundation/NSXPCConnection/resume()) method. The following code shows an implementation of the protocol’s [`accept(connection:)`](appextensionconfiguration/accept(connection:).md) method, which is where you put your connection code. In the code, the app extension configures the connection with a local object and the interface that both it and the host app recognize.

```swift
struct ExampleConfiguration<E:ExampleExtension>: AppExtensionConfiguration {
        
    // Determine whether to accept the XPC connection from the host.
    func accept(connection: NSXPCConnection) -> Bool {
        connection.exportedObject = myCustomObject
        connection.exportedInterface = NSXPCInterface(with: HostAppInterface.self)
        connection.resume()
        return true
    }
}
```

If the host app uses the [`XPC`](https://developer.apple.com/documentation/XPC) framework for communication, establish a connection using a [`ConnectionHandler`](connectionhandler.md) structure instead of a custom configuration type. The XPC framework is a lower-level version of the Foundation API that offers better options for communicating with hardened app extensions. The host app might require the use of this framework, especially if its extension point includes the [`AppExtensionPoint.EnhancedSecurity`](appextensionpoint/enhancedsecurity.md) attribute.

The following code shows the configuration of a text translation app extension that uses the [`XPC`](https://developer.apple.com/documentation/XPC) framework. The app extension’s configuration property returns a [`ConnectionHandler`](connectionhandler.md) type to process incoming requests. The provided closure creates a custom object to handle incoming requests and return a response. The app extension defines the `translate()` method to generate the translation for a host-provided string.

```swift
public extension MyTextTransformerExtension {
    var configuration: some AppExtensionConfiguration {
        return ConnectionHandler { request  in
            let handler = Handler(appex: self)
            return request.accept { session in
                return handler
            }
        }
    }
}

// Process text translation requests using an XPCSession.  
struct Handler<E: MyTextTransformerExtension>: XPCPeerHandler {
    let appex: E
    
    func handleIncomingRequest(_ input: TranslateMessage) -> (any Encodable)? {
        let text = input.text
        let result = appex.translate(text:text)
        return TranslateMessage.Response(translatedText: result)
    }
}

// The input message from the host app and the translation response.
struct TranslateMessage: Codable {
    let text: String
    
    struct Response: Codable {
        let translatedText: Text
    }
}
```

For more information about using XPC for communicating between processes, see the [`XPC`](https://developer.apple.com/documentation/XPC) framework and the [`XPC`](https://developer.apple.com/documentation/Foundation/xpc) in the Foundation framework.

## See Also

- [protocol AppExtension](appextension.md)
  An interface you use to declare the content, structure, and behavior of an app extension.
- [protocol AppExtensionConfiguration](appextensionconfiguration.md)
  An interface you use to configure the XPC connection in your app extension.
- [struct ConnectionHandler](connectionhandler.md)
  A type that contains a custom closure that handles incoming XPC connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/building-an-app-extension-to-support-a-host-app)*