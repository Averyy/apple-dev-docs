# ActiveNSExtensionsResponse.ExtensionsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains information about an extension.

**Availability**:
- macOS 10.13+

## Declaration

```
object ActiveNSExtensionsResponse.ExtensionsItem
```

## Properties

- `ContainerDisplayName` (string): The display name of the container.
- `ContainerIdentifier` (string): The identifier of the container.
- `DisplayName` (string) *(required)*: The extension’s display name.
- `ExtensionPoint` (string) *(required)*: The [`NSExtensionPointIdentifier`](../../BundleResources/information-property-list/nsextension/nsextensionpointidentifier.md) for the extension.
- `Identifier` (string) *(required)*: The identifier of the extension.
- `Path` (string) *(required)*: The path to the extension.
- `UserElection` (string) *(required)*: The user-selected state of the extension, which a user sets in the Extensions preference pane in System Preferences.

  **Allowed Values**: `Default`, `Use`, `Ignore`
- `Version` (string) *(required)*: The version of the extension.

## See Also

### Objects
- [object ActiveNSExtensionsResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activensextensionsresponse/extensionsitem)*