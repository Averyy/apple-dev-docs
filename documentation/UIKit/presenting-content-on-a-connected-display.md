# Presenting content on a connected display

**Framework**: UIKit

Fill connected displays with additional content from your app.

#### Overview

The user can connect additional displays to an iOS device at any time using AirPlay or a physical cable. Each additional display represents new space on which to present your app’s content. To present content on a connected display, you attach windows to [`UIWindowScene`](uiwindowscene.md) objects that the system provides and respond to life-cycle events using scene delegates.

UIKit defines different [`UISceneSession.Role`](uiscenesession/role-swift.struct.md) types to indicate how the user interacts with the content for a scene. The following types relate to content displayed on a connected screen:

- Scenes with the [`windowApplication`](uiscenesession/role-swift.struct/windowapplication.md) role present interactive windows. The windows render on the built-in display or a connected display for some iPad models. Windows for more than one scene may present concurrently and may not take up the full screen.
- Scenes with the [`windowExternalDisplayNonInteractive`](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) role present noninteractive windows on connected displays. When an app presents content for this scene, it spans the full screen.

##### Configure Your Project for Scenes

You provide the system with scene configurations to specify the information it uses to create scenes for your app and indicate the types of scenes your app supports.

By default, Xcode preconfigures new projects to use scenes with the [`windowApplication`](uiscenesession/role-swift.struct/windowapplication.md) role. iPad models with the M1 chip can present interactive content on the connected screen through this type of scene, when using Stage Manager, an external keyboard, and a pointing device.

To use the connected display to present noninteractive content that supplements the interactive content your app presents on the built-in screen, provide a new configuration for the [`windowExternalDisplayNonInteractive`](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) role. When an external display connects, the system provides an additional scene for your app to add the noninteractive content to. For example, a game might show its content on a connected display and show game controls on the built-in screen.

![An iPhone displays game controls while the game graphics are displayed on a connected television.](https://docs-assets.developer.apple.com/published/a228f29381d8cfc1afe87d40970ba29d/media-4030189%402x.png)

For more information, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

##### Attach a Window to a Scene

When a display connects to an iOS device, the system provides a scene for your app. Your app receives the scene through the [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md) method on your scene delegate. You can use the method and the session object it provides to configure and attach a window to the scene. The system displays the window you provide on the window scene’s current screen.

This example configures a window to render on a scene’s display.

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    guard let windowScene = (scene as? UIWindowScene) else { return }

    if session.role == .windowApplication {
        let window = UIWindow(windowScene: windowScene)
        window.rootViewController = ViewController()
        self.window = window
        window.makeKeyAndVisible()
    }
}
```

When using a storyboard, the system initializes and attaches a window to the scene for you.

In addition to calling this method, UIKit also posts the [`willConnectNotification`](uiscene/willconnectnotification.md) notification.

##### Handle Disconnection

When the system disconnects a scene from your app, which may occur if a user disconnects the display, your app receives a call through the [`sceneDidDisconnect(_:)`](uiscenedelegate/scenediddisconnect(_:).md) method on the scene’s delegate. Use this method to perform any final cleanup and update the content other scenes present, when necessary.

UIKit also posts the [`didDisconnectNotification`](uiscene/diddisconnectnotification.md) notification in addition to calling this method.

##### Handle Transitions to and From Connected Displays

Scenes may appear on different displays during their lifetime. If you use information from a [`UIScreen`](uiscreen.md) object, obtain it contextually using a windows scene’s [`screen`](uiwindowscene/screen.md) property.

Use the scene delegate’s [`windowScene(_:didUpdate:interfaceOrientation:traitCollection:)`](uiwindowscenedelegate/windowscene(_:didupdate:interfaceorientation:traitcollection:).md) method if your app needs to know when a scene is changing screens.

This examples uses a display link and updates the link when the scene changes screens.

```swift
class ExternalDisplaySceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    var screen: UIScreen?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = (scene as? UIWindowScene) else { return }

        if session.role == .windowExternalDisplayNonInteractive {
            let window = UIWindow(windowScene: windowScene)
            window.rootViewController = ExternalDisplayViewController()
            self.window = window
            window.makeKeyAndVisible()
            ...
            setupDisplayLinkIfNecessary()
        }
    }

    func windowScene(_ windowScene: UIWindowScene, didUpdate previousCoordinateSpace: UICoordinateSpace, interfaceOrientation previousInterfaceOrientation: UIInterfaceOrientation, traitCollection previousTraitCollection: UITraitCollection) {
        setupDisplayLinkIfNecessary()
    }

    weak var linkedScreen: UIScreen?

    func setupDisplayLinkIfNecessary() {
        let currentScreen = self.screen
        if currentScreen != linkedScreen {
            // Set up display link
            ...
            self.linkedScreen = currentScreen
        }
    }

    ...
}
```

##### Change the Screen Mode of an External Display

Many displays support multiple resolutions, some of which use different pixel aspect ratios. Screen objects use the most common screen mode by default, but they support changing that mode when they display content for a scene with the [`windowExternalDisplayNonInteractive`](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) role. For example, if you’re implementing a game using textures for a 640 x 480 pixel screen, you might change the screen mode for screens with higher default resolutions. Don’t attempt to change the mode of a screen for a scene with the [`windowApplication`](uiscenesession/role-swift.struct/windowapplication.md) role.

If you plan to use a screen mode other than the default one, apply that mode to the [`UIScreen`](uiscreen.md) object before associating the screen with a window. The [`UIScreenMode`](uiscreenmode.md) class defines the attributes of a single screen mode. You can get a list of the modes supported by a screen from its [`availableModes`](uiscreen/availablemodes.md) property and then iterate through the list for one that matches your needs.

For more information about screen modes, see [`UIScreenMode`](uiscreenmode.md).

## See Also

- [Multitasking on iPad](multitasking-on-ipad.md)
  Implement multitasking APIs to seamlessly integrate your app with iPadOS.
- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [class UIScreen](uiscreen.md)
  An object that defines the properties associated with a hardware-based display.
- [class UIScreenMode](uiscreenmode.md)
  A possible set of attributes that can apply to a screen object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/presenting-content-on-a-connected-display)*