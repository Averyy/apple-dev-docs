# UILaunchScreen

**Framework**: Bundle Resources  
**Kind**: dictionary

The user interface to show while an app launches.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

You use this key to define the launch screen that the system displays while your app launches. If you need to provide different launch screens in response to being launched by different URL schemes, use [`UILaunchScreens`](information-property-list/uilaunchscreens.md) instead.

> **Note**:  Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards, use [`UILaunchStoryboardName`](information-property-list/uilaunchstoryboardname.md) instead.

## Topics

### Main Interface
- [UIColorName](information-property-list/uilaunchscreen/uicolorname.md)
  The name of a color to use as the background color on the launch screen.
- [UIImageName](information-property-list/uilaunchscreen/uiimagename.md)
  The name of an image to display during app launch.
- [UIImageRespectsSafeAreaInsets](information-property-list/uilaunchscreen/uiimagerespectssafeareainsets.md)
  A Boolean that specifies whether the launch image should respect the safe area insets.
### Border Elements
- [UINavigationBar](information-property-list/uilaunchscreen/uinavigationbar.md)
  Navigation bar visibility and configuration during launch.
- [UITabBar](information-property-list/uilaunchscreen/uitabbar.md)
  Tab bar visibility and configuration during launch.
- [UIToolbar](information-property-list/uilaunchscreen/uitoolbar.md)
  Toolbar visibility and configuration during launch.

## See Also

- [UILaunchScreens](information-property-list/uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](information-property-list/uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](information-property-list/uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](information-property-list/uilaunchtofullscreenbydefaultonmac.md)
  A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen)*