# UILaunchToFullScreenByDefaultOnMac

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.

**Availability**:
- macOS 12.1+

## Details

- **Name**: `UILaunchToFullScreenByDefaultOnMac`
- **Type**: boolean

#### Discussion

To launch your iPad app in full-screen mode when running in macOS, add this key to your app’s `Info.plist` file and set its value to [`true`](../../Swift/true.md). State restoration can override this behavior if the person using your app exits full-screen mode before quitting the app.

You can also provide a pixel-perfect, edge-to-edge, full-screen experience by including the [`UISupportsTrueScreenSizeOnMac`](./uisupportstruescreensizeonmac.md) key with a value of [`true`](../../Swift/true.md) in your app’s `Info.plist` file.

[`UILaunchToFullScreenByDefaultOnMac`](./uilaunchtofullscreenbydefaultonmac.md) has no effect on your iPad app when:

- The app supports iPad multitasking and resizable windows. For more information, see [`UIRequiresFullScreen`](./uirequiresfullscreen.md).
- The app is running on other Apple platforms.
- The app is built with [Mac Catalyst](../../UIKit/mac-catalyst.md).

## See Also

### Launch interface
- [UILaunchScreen](./uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](./uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](./uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](./uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](./lsuipresentationmode.md)
  The initial user-interface mode for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchtofullscreenbydefaultonmac)*