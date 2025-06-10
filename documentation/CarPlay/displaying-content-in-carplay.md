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

If your app specifies the navigation entitlement, implement the [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) method instead because it provides a reference to your app’s window that CarPlay manages. Create an instance of your map-drawing view controller and set it as the window’s root view controller. Make sure that you set your interface controller’s root template.

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