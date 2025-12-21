# UILaunchToFullScreenByDefaultOnMac

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.

**Availability**:
- macOS 12.1+

#### Discussion

To launch your iPad app in full-screen mode when running in macOS, add this key to your app’s `Info.plist` file and set its value to [`true`](https://developer.apple.com/documentation/Swift/true). State restoration can override this behavior if the person using your app exits full-screen mode before quitting the app.

You can also provide a pixel-perfect, edge-to-edge, full-screen experience by including the [`UISupportsTrueScreenSizeOnMac`](information-property-list/uisupportstruescreensizeonmac.md) key with a value of [`true`](https://developer.apple.com/documentation/Swift/true) in your app’s `Info.plist` file.

[`UILaunchToFullScreenByDefaultOnMac`](information-property-list/uilaunchtofullscreenbydefaultonmac.md) has no effect on your iPad app when:

- The app supports iPad multitasking and resizable windows. For more information, see [`UIRequiresFullScreen`](information-property-list/uirequiresfullscreen.md).
- The app is running on other Apple platforms.
- The app is built with [`Mac Catalyst`](https://developer.apple.com/documentation/UIKit/mac-catalyst).

## See Also

- [UILaunchScreen](information-property-list/uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](information-property-list/uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](information-property-list/uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](information-property-list/uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchtofullscreenbydefaultonmac)*