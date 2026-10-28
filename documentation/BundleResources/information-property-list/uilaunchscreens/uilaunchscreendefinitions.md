# UILaunchScreenDefinitions

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

A collection of launch screen configuration dictionaries.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UILaunchScreenDefinitions` (Launch Screen Definitions)
- **Type**: array of dictionary 

## Discussion

Each dictionary in the array resembles the one you might define for the [`UILaunchScreen`](../uilaunchscreen.md) key, with the addition of a [`UILaunchScreenIdentifier`](./uilaunchscreendefinitions/uilaunchscreenidentifier.md) key that provides a unique identifier for the dictionary. You use that identifier when associating to the dictionary with a URL scheme in the [`UIURLToLaunchScreenAssociations`](./uiurltolaunchscreenassociations.md) array, or to indicate it as the default launch screen with the [`UIDefaultLaunchScreen`](./uidefaultlaunchscreen.md) key.

## Topics

### Identity
- [UILaunchScreenIdentifier](./uilaunchscreendefinitions/uilaunchscreenidentifier.md)
  A unique name for the launch screen configuration.
### Main Interface
- [UIColorName](./uilaunchscreendefinitions/uicolorname.md)
  The name of a color to use as the background color on the launch screen.
- [UIImageName](./uilaunchscreendefinitions/uiimagename.md)
  The name of an image to display during app launch.
- [UIImageRespectsSafeAreaInsets](./uilaunchscreendefinitions/uiimagerespectssafeareainsets.md)
  A Boolean that specifies whether the launch image should respect the safe area insets.
### Border Elements
- [UINavigationBar](./uilaunchscreendefinitions/uinavigationbar.md)
  Navigation bar visibility and configuration during launch.
- [UITabBar](./uilaunchscreendefinitions/uitabbar.md)
  Tab bar visibility and configuration during launch.
- [UIToolbar](./uilaunchscreendefinitions/uitoolbar.md)
  Toolbar visibility and configuration during launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens/uilaunchscreendefinitions)*