# NSExtensionFileProviderActions

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The custom actions for a File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Details

- **Name**: `NSExtensionFileProviderActions`
- **Type**: array of dictionary 

## Topics

### Action Configuration
- [NSExtensionFileProviderActionActivationRule](./nsextensionfileprovideractions/nsextensionfileprovideractionactivationrule.md)
  A predicate that determines whether a File Provider extension action appears in the context menu.
- [NSExtensionFileProviderActionIdentifier](./nsextensionfileprovideractions/nsextensionfileprovideractionidentifier.md)
  A unique identifier for a File Provider extension action.
- [NSExtensionFileProviderActionName](./nsextensionfileprovideractions/nsextensionfileprovideractionname.md)
  The localized name for a File Provider extension action that appears in the context menu.

## See Also

### File Provider
- [NSExtensionFileProviderDocumentGroup](./nsextensionfileproviderdocumentgroup.md)
  The identifier of a shared container that can be accessed by a Document Picker extension and its associated File Provider extension.
- [NSExtensionFileProviderSupportsEnumeration](./nsextensionfileprovidersupportsenumeration.md)
  A Boolean value that indicates whether a File Provider extension enumerates its content.
- [NSExtensionFileProviderDownloadPipelineDepth](./nsextensionfileproviderdownloadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to fetch data from remote storage.
- [NSExtensionFileProviderUploadPipelineDepth](./nsextensionfileprovideruploadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to upload data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionfileprovideractions)*