# Building your app’s initial CarPlay interface

**Framework**: CarPlay  
**Role**: Article

Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.

## Overview

Create your app’s CarPlay experience by adding CarPlay-specific scenes to your existing iOS app. A CarPlay app is not a standalone app; it’s an integral part of your iOS app and has access to all the same data. When someone opens your app in a CarPlay environment, the system launches your iOS app and instantiates its main CarPlay scene. You respond by configuring that scene with your CarPlay-specific content.

Build your app’s CarPlay interface from *templates*, which the CarPlay framework provides for the different types of information you might display from your app. When you present one of these templates, CarPlay renders it with the content you provide and sends the results to the vehicle or HomeView display. The rendering process takes into account differences between display sizes and environment settings. For example, CarPlay automatically renders your content with a light or dark appearance based on vehicle or ambient light settings.

> **Note**: Apps require specific entitlements to run in a CarPlay environment. For information about how to request the entitlements you need, see [Preparing your iOS app for CarPlay development](./preparing-your-ios-app-for-carplay-development.md).

## Define a CarPlay scene delegate object

At app launch, CarPlay creates your app’s main scene object and a custom delegate object you define and use to manage life-cycle events for the scene. The CarPlay framework defines the types for scene objects, and you define the delegate by adding the [`CPTemplateApplicationSceneDelegate`](./cptemplateapplicationscenedelegate.md) protocol to one of your app-specific types. The protocol defines the methods to set up and tear down your CarPlay app and its interface.

In addition to creating your scene object, CarPlay creates a [`CPInterfaceController`](./cpinterfacecontroller.md) object and delivers it to your delegate object. The interface controller object contains information about the CarPlay environment, and you call its methods to install your app’s initial interface and change that interface later. For all apps except navigation apps, CarPlay delivers this object to your delegate’s [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) method. The following code shows a minimal implementation of a delegate object and this method that store a reference to the interface controller:

```swift
class MySceneDelegate : NSObject, CPTemplateApplicationSceneDelegate {
    private var interfaceController : CPInterfaceController? = nil

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, 
            didConnect interfaceController: CPInterfaceController) {
        self.interfaceController = interfaceController

    }

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
                                  didDisconnectInterfaceController interfaceController: CPInterfaceController) {
        self.interfaceController = nil
    }
}
```

In a navigation app, CarPlay calls the [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method of your delegate instead of the [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) method. The two methods serve the same purpose, but the [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method receives a window object in addition to the interface controller. Navigation apps use this window to specify their custom map content, and use the interface controller to specify the rest of their interface. The following example shows a minimal implementation of the scene delegate that stores references to both objects:

```swift
class MySceneDelegate : NSObject, CPTemplateApplicationSceneDelegate {
    private var interfaceController : CPInterfaceController? = nil
    private var window : CPWindow? = nil

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
                                  didConnect interfaceController: CPInterfaceController,
                                  to window: CPWindow) {
        self.interfaceController = interfaceController
        self.window = window
    }
    
    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
                                  didDisconnect interfaceController: CPInterfaceController,
                                  from window: CPWindow) {
        self.interfaceController = nil
        self.window = nil
    }
}
```

> ❗ **Important**: Implement only a single connection and disconnection method for your app. CarPlay calls the [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method only for navigation apps, and calls the [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) method for all other app types.

## Add the scene details to your app’s information property list

CarPlay creates your app’s initial scene and delegate object at startup, but it gets the information about these types from your app’s [application scene manifest](../BundleResources/information-property-list/uiapplicationscenemanifest.md). CarPlay requires apps to support scenes, and the application scene manifest defines the scenes your app offers and the class names of the associated scene and delegate objects. Add your app’s main CarPlay scenes to this manifest using the [`CPTemplateApplicationSceneSessionRoleApplication`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md) key.

The following code shows the CarPlay-specific keys and values for the app’s main scene. Include the [`UIApplicationSupportsMultipleScenes`](../BundleResources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) key with a value of `true` to tell the system your app declares both iOS and CarPlay scenes. For the [`CPTemplateApplicationSceneSessionRoleApplication`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md) key, the scene class name is always [`CPTemplateApplicationScene`](./cptemplateapplicationscene.md) because CarPlay provides this type. Set the delegate class name to the type you defined previously.

```plist
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <true/>
    <key>UISceneConfigurations</key>
    <dict>
        <key>CPTemplateApplicationSceneSessionRoleApplication</key>
        <array> 
            <dict>
                <key>UISceneClassName</key>
                <string>CPTemplateApplicationScene</string>
                <key>UISceneDelegateClassName</key>
                <string>$(PRODUCT_MODULE_NAME).MySceneDelegate</string> 
                <key>UISceneConfigurationName</key>
                <string>Default Configuration</string>
            </dict>
        </array>
        // ... iOS app scenes
    </dict>
</dict>     
```

In addition to a main scene, navigation apps can add scenes for the CarPlay Dashboard and instrument cluster. To specify a scene for the CarPlay Dashboard, add the [`CPTemplateApplicationDashboardSceneSessionRoleApplication`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md) key to your app’s manifest. If your app can show map content in the vehicle’s instrument cluster, add the [`CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md) key. CarPlay instantiates these scenes on demand to support the associated features.

For information about how to configure your project’s information property list file, see [Managing your app’s information property list values](../BundleResources/managing-your-app-s-information-property-list.md).

## Set the root template of your CarPlay interface

When your CarPlay app launches, the system creates your delegate object and calls its [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) or [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method. These methods act as the entry point for your CarPlay app, and you use them to initialize any required data and provide your app’s initial interface. Perform any startup tasks as quickly as possible, and set your app’s initial interface using the [`setRootTemplate(_:animated:completion:)`](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md) method of the provided interface controller object.

Specify the content for your app’s initial interface using one of the custom templates CarPlay provides. You can install any template as the root template of your interface, but the [`CPTabBarTemplate`](./cptabbartemplate.md) or [`CPListTemplate`](./cplisttemplate.md) types are the most common choices for apps with hierarchical content. If you’re creating a navigation app, install a [`CPMapTemplate`](./cpmaptemplate.md) object as the root template. The following example creates a tab bar template for an audio app and fills each tab with a list template that arranges content in a specific way.

```swift
func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, 
        didConnect interfaceController: CPInterfaceController) {
            
    self.interfaceController = interfaceController
            
    // Create list templates for each tab in the interface.
    let tab1 = playlistTemplate()
    let tab2 = albumListTemplate()
    let tab3 = songListTemplate()
    let tab4 = artistListTemplate()
        
    // Configure a tab bar template as the root template.
    let tabBarTemplate = CPTabBarTemplate(templates: [tab1, tab2, tab3, tab4])
    tabBarTemplate.delegate = self

    interfaceController.setRootTemplate(tabBarTemplate, animated: false, completion: nil)
}
```

During your app’s initial setup, CarPlay presents your root template without animations even if you specify `true` for the `animated` parameter. If you change your app’s root template later, you can animate the appearance of the new template to create a smoother transition between the new and old template.

## Configure the map content in a navigation app

Navigation apps perform one additional setup step in their delegate’s [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method. In addition to assigning a [`CPMapTemplate`](./cpmaptemplate.md) object as the interface’s root template, the app needs to install its custom map content in the provided [`CPWindow`](./cpwindow.md) object. To provide this content, define a custom [`UIViewController`](../UIKit/uiviewcontroller.md) type that displays your map tiles or other navigation-related content. The window is an instance of the [`UIWindow`](../UIKit/uiwindow.md) type, so install your view controller by assigning it to the window’s [`rootViewController`](../UIKit/uiwindow/rootviewcontroller.md) property. The following code creates a map view controller and installs it in the provided window. The delegate method also configures a map template to display overlays and other information on top of the map content.

```swift
class MySceneDelegate : NSObject, CPTemplateApplicationSceneDelegate {
    private var interfaceController : CPInterfaceController? = nil
    private var window : CPWindow? = nil

    func makeMapViewController() -> MapViewController {
        return MapViewController()
    }

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
            didConnect interfaceController: CPInterfaceController,
            to window: CPWindow) {
    self.interfaceController = interfaceController
    self.window = window
        
    window.rootViewController = makeMapViewController()
        
    let mapTemplate = CPMapTemplate()
    mapTemplate.mapDelegate = self
    interfaceController.setRootTemplate(mapTemplate, animated: true, completion: nil)
}
```

In a navigation app, keep your map content separate from the routes and other information you display on top of the map. When someone interacts with your app, CarPlay reports the interactions to the [`CPMapTemplate`](./cpmaptemplate.md) object, which forwards specific interactions to its delegate object. To synchronize your map content with the map template, provide a delegate object and use it to handle navigation-related events. You can also use it to handle map-related manipulations such as pan, zoom, rotate, and pitch gestures. For more information about how to implement the delegate, see the [`CPMapTemplateDelegate`](./cpmaptemplatedelegate.md) class.

## Explore the templates available to your app

The CarPlay framework templates give you different ways to display your app’s content, but the type of app you create determines which templates you can use to build your interface. All apps have access to templates that display general information, such as the list, grid, and tab bar templates. These templates are particularly useful for helping people navigate layers of hierarchical content. Other templates are available only when an app has a legitimate need to display the associated type of information. For example, audio and video apps can display the [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object, but an EV charging app can’t. The following table shows the available templates for each app type.

| Template | Audio, video | Communication | Driving task, voice-based conversation | EV charging, fueling, parking | Quick food ordering | Public safety | Navigation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Action sheet | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Alert | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Grid | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| List | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tab bar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Voice control | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Contact |  | ✅ |  |  |  | ✅ | ✅ |
| Information |  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Map |  |  |  |  |  |  | ✅ |
| Now playing | ✅ | ✅ |  |  |  | ✅ |  |
| Point of interest |  |  | ✅ | ✅ | ✅ | ✅ |  |
| Search | ✅ |  |  | ✅ |  | ✅ | ✅ |

CarPlay employs a navigation-style interface for all apps, and maintains a navigation stack of the templates you display. With this type of interface, the root template you install becomes the first template on the stack. Each time you add, or *push*, a template onto the stack, CarPlay updates your interface to display the content for the newly pushed template. When you remove, or *pop*, a template off the stack, CarPlay displays the template that’s now at the top of the stack. You can pop all templates off the stack except the root template.

To prevent overly complex interfaces, CarPlay limits the number of templates you can push onto your app’s navigation stack. The root template counts as the first template on the navigation stack. Audio, communication, EV charging, parking, public safety, and navigation apps can push four additional templates onto the stack. Fueling and voice-based conversational apps can push two additional templates. Driving and quick-food ordering apps can push two additional templates in iOS 26.4, but only one template in iOS 26.3 and earlier.

## See Also

### App management
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/building-your-apps-initial-carplay-interface)*