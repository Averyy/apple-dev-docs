# UILaunchStoryboards

**Framework**: Bundle Resources  
**Kind**: dictionary

The launch storyboard to use to generate a launch image when your app opens from a supported scheme.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

#### Discussion

Use [`UILaunchStoryboards`](information-property-list/uilaunchstoryboards.md) when you want your app to show a different launch screen for different schemes. The schemes are the ones specified in your app’s [`CFBundleURLTypes`](information-property-list/cfbundleurltypes.md). You can also specify a default launch storyboard.

If your app has a single launch storyboard, use the simpler [`UILaunchStoryboardName`](information-property-list/uilaunchstoryboardname.md) instead.

## Topics

### Specifying Launch Storyboards
- [UILaunchStoryboardDefinitions](information-property-list/uilaunchstoryboards/uilaunchstoryboarddefinitions.md)
  An array of dictionaries mapping launch storyboard identifiers to storyboards.
- [UIDefaultLaunchStoryboard](information-property-list/uilaunchstoryboards/uidefaultlaunchstoryboard.md)
  The identifier of the default launch storyboard to use.
### Associating Storyboard Identifiers with Schemes
- [UIURLToLaunchStoryboardAssociations](information-property-list/uilaunchstoryboards/uiurltolaunchstoryboardassociations.md)
  The user-defined storyboard identifiers that associate with supported schemes.

## See Also

- [UILaunchScreen](information-property-list/uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](information-property-list/uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](information-property-list/uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](information-property-list/uilaunchtofullscreenbydefaultonmac.md)
  A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboards)*