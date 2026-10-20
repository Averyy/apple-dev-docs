# UIURLToLaunchStoryboardAssociations

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The user-defined storyboard identifiers that associate with supported schemes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Details

- **Name**: `UIURLToLaunchStoryboardAssociations`
- **Type**: dictionary

#### Discussion

The keys for this dictionary are the URL schemes defined in [`CFBundleURLTypes`](../cfbundleurltypes.md) for your app. The value for the specified key is a [`UILaunchStoryboardIdentifier`](./uilaunchstoryboarddefinitions/uilaunchstoryboardidentifier.md) from the [`UILaunchStoryboardDefinitions`](./uilaunchstoryboarddefinitions.md) array.

## Properties

- `Any Key` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboards/uiurltolaunchstoryboardassociations)*