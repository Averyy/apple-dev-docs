# Adding a settings interface to your app

**Framework**: Foundation

Create a dedicated interface to display and modify your app’s settings.

#### Overview

If your app has configurable settings, add a settings interface to give people a way to edit them. A settings interface explains the purpose of each setting and offers buttons, sliders, text fields, and other controls to change the associated values. Typically, you include a settings interface as part of your app’s UI. However, some platforms allow you to display your app’s settings in the system’s Settings app. You might choose the Settings app for settings people change infrequently, or if you prefer not to include a settings interface in your app.

For information about how to design a settings interface, see [`Settings`](https://developer.apple.com/design/Human-Interface-Guidelines/settings) in Human Interface Guidelines.

##### Add a Settings Window to Your Macos App

In macOS, apps display settings in a separate window that’s accessible from the app’s menus. The standard App menu includes space for a Settings menu item, which displays your settings window when selected.

To define the settings interface of your macOS app using SwiftUI, add a [`Settings`](https://developer.apple.com/documentation/SwiftUI/Settings) scene to the body of your app. When this scene type is present in your app, SwiftUI updates your app’s menus to include an item to display your settings interface. When someone selects that menu item, SwiftUI displays a new window with the contents of the scene you provide. The following code shows a settings scene in the body of a SwiftUI app:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}
```

When building the contents of a settings scene in SwiftUI, add the [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) property wrapper to variables that store settings. This property wrapper synchronizes the value of the specified setting with the variable’s value. You can then use the variable as the value of the relevant control in your scene. When someone changes the control’s value, SwiftUI automatically writes the new value back to the defaults database. SwiftUI also detects changes that occur outside of your app and refreshes your settings interface in response.

If you build your app using AppKit, add a window and view controllers with your settings content. New AppKit projects in Xcode contain a menu item for opening your settings interface, but don’t configure that menu item initially. Build your settings interface using a window and view controller and connect it to the menu item. Configure the controls of your view controller using your [`UserDefaults`](userdefaults.md) object. When someone changes the value of a control, write the new value back to that defaults object.

For information about how to access settings in your interface, see [`Accessing settings from your code`](accessing-settings-from-your-code.md). For more information about AppKit view controllers, see [`NSViewController`](https://developer.apple.com/documentation/AppKit/NSViewController).

##### Integrate Settings Into Your Apps Ui on Other Platforms

There is no standard way to display settings from apps in iOS, iPadOS, tvOS, visionOS, or watchOS. In macOS, you typically display settings in a separate window that people access from your menus. However, this approach doesn’t work as well on other Apple platforms, many of which don’t display menus or offer windows people can manipulate directly. To build a settings interface on these platforms, consider how people use the underlying settings in your app:

- If people change settings frequently, make your settings interface readily available from your app’s main UI. For example, a game’s main screen might include a control to display game controls and other settings.
- If people change settings occasionally, include settings in a separate scene or view controller that you display only as needed. For example, an app with a tab bar interface might add a tab for settings.
- If people change settings infrequently, move them to the system’s [`Display settings in the system’s Settings app`](adding-a-settings-interface-to-your-app#Display-settings-in-the-systems-Settings-app.md). The Settings app provides a dedicated space for each app that includes both system- and app-specific settings.
- In a watchOS app, minimize the need for modifying settings by choosing reasonable default values. If you do need a settings interface, integrate it into your app’s UI.

When building a settings interface of any kind, use a dedicated scene or view controller to manage the interface and any relevant changes. Using a dedicated scene provides a clean separation between your settings code and the rest of your code. The defaults system has notification mechanisms to help you update your app when settings change. For more information about detecting these changes, see [`Accessing settings from your code`](accessing-settings-from-your-code.md).

##### Display Settings in the Systems Settings App

In iOS, iPadOS, tvOS, and visionOS, you can optionally display your settings from the system’s Settings app. The Settings app provides a dedicated page for each app, and this page includes system-level settings for location, notifications, and other system technologies your app uses. You can add app-specific settings to this space, but typically do so only for settings people change infrequently. You might also use the system Settings app if you don’t want to display settings in your app’s UI.

To add your app-specific settings to the system Settings app, include a Settings bundle inside your app. A  is a bundle directory with property list files and other files that describe your settings interface to the system. The system uses this content to build the interface for your app-specific settings, and to map each control in that interface to a specific setting in your defaults database. When people make changes in the Settings app, the system updates your app’s defaults database accordingly.

> **Note**: In an iOS app running in Mac Catalyst, the system constructs a settings interface from the contents of your Settings bundle, and adds a Settings menu item to your app’s menus. When someone selects the menu item, the system displays the settings interface and manages interactions for you.

When you want to display an app’s settings, you need to ask the system to open the Settings app and show your custom page. You do this with the help of the app object’s [`openSettingsURLString`](https://developer.apple.com/documentation/UIKit/UIApplication/openSettingsURLString) property, which contains a deep link to your custom settings page. Create a URL using this value and pass that URL to the [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/open(_:options:completionHandler:)) method when you’re ready to display your settings.

For information about how to create a Settings bundle, see [`Building a Settings bundle for your app`](building-a-settings-bundle-for-your-app.md).

## See Also

- [Building a Settings bundle for your app](building-a-settings-bundle-for-your-app.md)
  Integrate your app’s custom settings into the Settings app in iOS, iPadOS, tvOS, and visionOS, and support a Mac Catalyst settings window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/adding-a-settings-interface-to-your-app)*