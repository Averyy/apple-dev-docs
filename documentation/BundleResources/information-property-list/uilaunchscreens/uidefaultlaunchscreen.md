# UIDefaultLaunchScreen

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The default launch screen configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UIDefaultLaunchScreen` (Default Screen Identifier)
- **Type**: string

## Discussion

Provide the identifier, stored in the [`UILaunchScreenIdentifier`](./uilaunchscreendefinitions/uilaunchscreenidentifier.md) key, of one of the launch screen definitions in your [`UILaunchScreenDefinitions`](./uilaunchscreendefinitions.md) array. The system displays the named launch screen when launching your app in response to a URL scheme that you don’t enumerate in the [`UIURLToLaunchStoryboardAssociations`](../uilaunchstoryboards/uiurltolaunchstoryboardassociations.md) dictionary, or when the user launches your app directly.

## See Also

### Associations
- [UIURLToLaunchScreenAssociations](./uiurltolaunchscreenassociations.md)
  The mapping of URL schemes to launch screen configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens/uidefaultlaunchscreen)*