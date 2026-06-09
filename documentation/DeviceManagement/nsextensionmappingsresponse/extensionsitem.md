# NSExtensionMappingsResponse.ExtensionsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains information about an extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object NSExtensionMappingsResponse.ExtensionsItem
```

## Properties

- `DisplayName` (string) *(required)*: The display name of the extension.
- `ExtensionPoint` (string) *(required)*: The [`NSExtensionPointIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionPointIdentifier) for the extension.
- `Identifier` (string) *(required)*: The identifier of the extension.

## See Also

- [object NSExtensionMappingsResponse.ErrorChainItem](nsextensionmappingsresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmappingsresponse/extensionsitem)*