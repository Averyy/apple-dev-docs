# UILaunchScreens

**Framework**: Bundle Resources  
**Kind**: dictionary

The user interfaces to show while an app launches in response to different URL schemes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

You use this key if your app supports launching in response to one or more URL schemes, and if you want to provide different launch screens for different launch triggers. If you need only one launch screen, use [`UILaunchScreen`](information-property-list/uilaunchscreen.md) instead.

To define launch screens, create an array of dictionaries, each similar to the one you might provide for [`UILaunchScreen`](information-property-list/uilaunchscreen.md), but with an added [`UILaunchScreenIdentifier`](information-property-list/uilaunchscreens/uilaunchscreendefinitions/uilaunchscreenidentifier.md) key that uniquely identifies the screen. Store the array as the value for the [`UILaunchScreenDefinitions`](information-property-list/uilaunchscreens/uilaunchscreendefinitions.md) key.

To map from URL schemes to a launch screens, create a dictionary of schemes and identifiers, and store it as the value for the [`UIURLToLaunchScreenAssociations`](information-property-list/uilaunchscreens/uiurltolaunchscreenassociations.md) key. Additionally, indicate a default launch screen by setting a value for the [`UIDefaultLaunchScreen`](information-property-list/uilaunchscreens/uidefaultlaunchscreen.md) key.

> **Note**:  Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards to define the launch screen, use the [`UILaunchStoryboards`](information-property-list/uilaunchstoryboards.md) key instead.

 Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards to define the launch screen, use the [`UILaunchStoryboards`](information-property-list/uilaunchstoryboards.md) key instead.

## Topics

### Launch Screen Definitions
- [UILaunchScreenDefinitions](information-property-list/uilaunchscreens/uilaunchscreendefinitions.md)
  A collection of launch screen configuration dictionaries.
### Associations
- [UIURLToLaunchScreenAssociations](information-property-list/uilaunchscreens/uiurltolaunchscreenassociations.md)
  The mapping of URL schemes to launch screen configurations.
- [UIDefaultLaunchScreen](information-property-list/uilaunchscreens/uidefaultlaunchscreen.md)
  The default launch screen configuration.

## See Also

- [UILaunchScreen](information-property-list/uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchStoryboardName](information-property-list/uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](information-property-list/uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](information-property-list/uilaunchtofullscreenbydefaultonmac.md)
  A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens)*