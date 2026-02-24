# Displaying Content in CarPlay

**Framework**: CarPlay

Use scenes to present your app’s content on the vehicle’s built-in screen.

#### Overview

A scene manages your CarPlay-enabled app’s user interface, including the window that CarPlay displays on the vehicle’s screen. Navigation apps are the only app category that have access to this window, and use it to draw their map content. All other categories of apps use only the scene’s interface controller to manage their user interface.

As CarPlay manages your app’s scene, you provide a scene delegate — an object that conforms to the [`CPTemplateApplicationSceneDelegate`](cptemplateapplicationscenedelegate.md) protocol — that the system notifies about scene life cycle events. CarPlay creates your app’s scene and scene delegate when the user launches your app.

##### Add a Carplay Scene

To add a CarPlay scene, provide its configuration in the scene manifest of your Xcode project’s `Info.plist` file. Specify your scene delegate’s class name as the value of the `UISceneDelegateClassName` key.

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
                <key>UISceneConfigurationName</key>
                <string>MyCarPlaySceneConfiguration</string>
                <key>UISceneDelegateClassName</key>
                <string>MyCarPlaySceneDelegate</string> 
            </dict>
        </array>
    </dict>
</dict>     
```

In your scene delegate, implement the [`templateApplicationScene(_:didConnect:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md) method and use the interface controller that it provides to set your root template.

**Swift**:

```swift
func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, 
    didConnect interfaceController: CPInterfaceController) {
    
    // Store a reference to the interface controller so 
    // you can add and remove templates as the user 
    // interacts with your app.
    self.interfaceController = interfaceController
    
    // Create a template and set it as the root.
    let rootTemplate = self.makeRootTemplate()
    interfaceController.setRootTemplate(rootTemplate, animated: true, 
        completion: nil)
}
```

**Obj-C**:

```objc
- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene 
   didConnectInterfaceController:(CPInterfaceController *)interfaceController {
    
    // Store a reference to the interface controller so 
    // you can add and remove templates as the user 
    // interacts with your app.
    self.interfaceController = interfaceController;
    
    // Create a template and set it as the root.
    CPTemplate *rootTemplate = [self makeRootTemplate];
    [self.interfaceController setRootTemplate:rootTemplate 
                                     animated:YES
                                   completion:NULL];
}
```

If your app specifies the navigation entitlement, implement the [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) method instead because it provides a reference to your app’s window that CarPlay manages. Create an instance of your map-drawing view controller and set it as the window’s root view controller. Make sure that you set your interface controller’s root template.

**Swift**:

```swift
func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene, 
    didConnect interfaceController: CPInterfaceController, to window: CPWindow) {
    
    // Retain references to the interface controller and window for
    // the entire duration of the CarPlay session.
    self.interfaceController = interfaceController
    self.carWindow = window
    
    // Assign the window's root view controller to the view controller
    // that draws your map content.
    window.rootViewController = MapRenderingViewController()
    
    // Create a map template and set it as the root.
    let mapTemplate = self.makeMapTemplate()
    interfaceController.setRootTemplate(mapTemplate, animated: true, 
        completion: nil)
}
```

**Obj-C**:

```objc
- (void)templateApplicationScene:(CPTemplateApplicationScene *)templateApplicationScene 
   didConnectInterfaceController:(CPInterfaceController *)interfaceController 
                        toWindow:(CPWindow *)window {
    
    // Retain references to the interface controller and window for
    // the entire duration of the CarPlay session.
    self.interfaceController = interfaceController;
    self.carWindow = window;
    
    // Assign the window's root view controller to the view controller
    // that draws your map content.
    window.rootViewController = [[MapRenderingViewController alloc] init];
    
    // Create a map template and set it as the root.
    CPMapTemplate *mapTemplate = [self makeMapTemplate];
    [interfaceController setRootTemplate:mapTemplate 
                                animated:YES
                              completion:NULL];
}
```

> ❗ **Important**:  Use the window’s root view controller to draw only map content. Don’t render alerts, overlays, or any other user interface elements. Use only the templates that the framework provides to create your app’s CarPlay user interface.

##### Add a Carplay Dashboard Scene

Navigation apps can add an additional scene entry to their scene manifest to enable their maps, upcoming maneuvers, and shortcut buttons to appear in the CarPlay Dashboard.

Add the following key to the `UIApplicationSceneManifest` dictionary in your Xcode project’s `Info.plist` file to specify that your app supports the CarPlay Dashboard:

```plist
<key>UIApplicationSceneManifest</key>
<dict>
    <key>CPSupportsDashboardNavigationScene</key>
    <true/>
</dict>
```

In the same file, add the CarPlay Dashboard scene configuration to the `UISceneConfigurations` dictionary. Provide your dashboard scene delegate’s class name as the value of the `UISceneDelegateClassName` key.

```plist
<key>CPTemplateApplicationDashboardSceneSessionRoleApplication</key>
<array> 
    <dict>
        <key>UISceneClassName</key>
        <string>CPTemplateApplicationDashboardScene</string>
        <key>UISceneConfigurationName</key>
        <string>MyCarPlayDashboardSceneConfiguration</string>
        <key>UISceneDelegateClassName</key>
        <string>MyCarPlayDashboardSceneDelegate</string> 
    </dict>
</array>
```

> 💡 **Tip**:  The names of the dashboard scene’s session role and scene class are different from the standard CarPlay scene. If the CarPlay Dashboard doesn’t display your navigation app, make sure that you’re using the correct names.

In your dashboard scene delegate, implement [`templateApplicationDashboardScene(_:didConnect:to:)`](cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene(_:didconnect:to:).md). Use the window that the method provides to render your map content. Set the dashboard controller’s [`shortcutButtons`](cpdashboardcontroller/shortcutbuttons.md) property to an array of buttons — up to a maximum of two — that the CarPlay Dashboard displays when your app isn’t actively navigating.

**Swift**:

```swift
func templateApplicationDashboardScene(_ templateApplicationDashboardScene: CPTemplateApplicationDashboardScene,
    didConnect dashboardController: CPDashboardController, to window: UIWindow) {
    
    // Retain references to the dashboard controller and window for
    // the entire duration of the CarPlay Dashboard session.
    self.dashboardController = dashboardController
    self.dashboardWindow = window
    
    // Assign the window's root view controller to the view controller
    // that draws your map content.
    window.rootViewController = MapRenderingViewController()
    
    // Create your shortcut buttons and add them to the dashboard.
    dashboardController.shortcutButtons = makeShortcutButtons()
}
```

**Obj-C**:

```objc
-(void)templateApplicationDashboardScene:(CPTemplateApplicationDashboardScene*)templateApplicationDashboardScene
           didConnectDashboardController:(CPDashboardController *)dashboardController 
                                toWindow:(UIWindow *)window {
    
    // Retain references to the dashboard controller and window for
    // the entire duration of the CarPlay Dashboard session.
    self.dashboardController = dashboardController;
    self.dashboardWindow = window;
    
    // Assign the window's root view controller to the view controller
    // that draws your map content.
    window.rootViewController = [[MapRenderingViewController alloc] init];
    
    // Create your shortcut buttons and add them to the dashboard.
    dashboardController.shortcutButtons = [self makeShortcutButtons];
}
```

## See Also

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay)*