# UIURLToLaunchScreenAssociations

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The mapping of URL schemes to launch screen configurations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UIURLToLaunchScreenAssociations` (URL to Launch Screen Associations)
- **Type**: dictionary

## Discussion

Set the keys of this dictionary to the URL schemes that your app supports. Provide a value for each key that is the identifier, stored in the [`UILaunchScreenIdentifier`](./uilaunchscreendefinitions/uilaunchscreenidentifier.md) key, of one of the launch screen definitions in your [`UILaunchScreenDefinitions`](./uilaunchscreendefinitions.md) array.

## Properties

- `Any Key` (string)

## See Also

### Associations
- [UIDefaultLaunchScreen](./uidefaultlaunchscreen.md)
  The default launch screen configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens/uiurltolaunchscreenassociations)*