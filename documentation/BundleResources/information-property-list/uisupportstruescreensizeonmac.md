# UISupportsTrueScreenSizeOnMac

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.

**Availability**:
- macOS 12.1+

## Details

- **Name**: `UISupportsTrueScreenSizeOnMac`
- **Type**: boolean

#### Discussion

To declare support for arbitrary screen sizes and resolutions when running your iPad app in macOS, add this key to your app’s `Info.plist` file and set its value to [`true`](../../Swift/true.md). This key has no effect when:

- The app supports iPad multitasking and resizable windows. For more information, see [`UIRequiresFullScreen`](./uirequiresfullscreen.md).
- The app is running on other Apple platforms.
- The app is built with [Mac Catalyst](../../UIKit/mac-catalyst.md).

The use of this key implies that your app is capable of handling a variety of display configurations available on a Mac, including:

- Small to large display resolutions; for example, 640 x 480 to 8K and beyond.
- Retina and non-Retina displays.
- All conceivable aspect ratios, including portrait and 21:9 ultrawide.

Use of the [`UISupportsTrueScreenSizeOnMac`](./uisupportstruescreensizeonmac.md) key also implies that your app is capable of handling portrait and landscape sizes even when they don’t align with the device orientation. For instance, if your app supports rotation in iPadOS, the device orientation is always landscape even though the display might have a portrait aspect ratio in reality.

> **Note**:  When running your iPad app on a Mac, macOS chooses the device orientation of your app from the set of app-supported orientations for iOS, regardless of the actual Mac display aspect ratio. This means that you don’t need to update the set of iOS-supported orientations (see [`UISupportedInterfaceOrientations`](./uisupportedinterfaceorientations.md)), or alter your code to handle unsupported orientations when using the [`UISupportsTrueScreenSizeOnMac`](./uisupportstruescreensizeonmac.md) key.

When you include [`UISupportsTrueScreenSizeOnMac`](./uisupportstruescreensizeonmac.md) in your app, your app is responsible for:

- Handling memory management concerns that may occur when running at extreme resolutions.
- Handling layout concerns for different aspect ratios, such as correct button placement.
- Letterboxing and pillarboxing as needed if your app requires a specific aspect ratio.

To provide a pixel-perfect, edge-to-edge, full-screen experience, use [`UISupportsTrueScreenSizeOnMac`](./uisupportstruescreensizeonmac.md) along with the [`UILaunchToFullScreenByDefaultOnMac`](./uilaunchtofullscreenbydefaultonmac.md) key.

## See Also

### Main user interface
- [UIApplicationSceneManifest](./uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [UIApplicationPreferredDefaultSceneSessionRole](./uiapplicationpreferreddefaultscenesessionrole.md)
  The preferred initial scene session role for your app.
- [NSMainStoryboardFile](./nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](./uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](./nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](./lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportstruescreensizeonmac)*