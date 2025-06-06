# UILaunchStoryboardName

**Framework**: Bundle Resources  
**Kind**: typealias

The filename of the storyboard from which to generate the app’s launch image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- tvOS 9.0+
- watchOS 2.0+

#### Discussion

Specify the name of the storyboard file without the filename extension. For example, if the filename of your storyboard is `LaunchScreen.storyboard`, specify “LaunchScreen” as the value for this key.

If you prefer to configure your app’s launch screen without storyboards, use [`UILaunchScreen`](information-property-list/uilaunchscreen.md) instead.

## See Also

- [UILaunchScreen](information-property-list/uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](information-property-list/uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboards](information-property-list/uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](information-property-list/uilaunchtofullscreenbydefaultonmac.md)
  A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboardname)*