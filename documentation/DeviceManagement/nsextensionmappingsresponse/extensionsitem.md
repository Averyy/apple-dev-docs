# NSExtensionMappingsResponse.ExtensionsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains information about an extension.

**Availability**:
- macOS 10.13+

## Declaration

```
object NSExtensionMappingsResponse.ExtensionsItem
```

## Properties

- `DisplayName` (string) *(required)*: The display name of the extension.
- `ExtensionPoint` (string) *(required)*: The [`NSExtensionPointIdentifier`](../../BundleResources/information-property-list/nsextension/nsextensionpointidentifier.md) for the extension.
- `Identifier` (string) *(required)*: The identifier of the extension.

## See Also

### Objects
- [object NSExtensionMappingsResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmappingsresponse/extensionsitem)*