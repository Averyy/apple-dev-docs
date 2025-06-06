# NSExtensionFileProviderUploadPipelineDepth

**Framework**: Bundle Resources  
**Kind**: typealias

The per-domain limit of concurrent calls that a file provider extension can make to upload data.

**Availability**:
- macOS 12.0+

#### Discussion

Use this value to set the limit of concurrent calls to methods like [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderReplicatedExtension/createItem(basedOn:fields:contents:options:request:completionHandler:)) and [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](https://developer.apple.com/documentation/FileProvider/NSFileProviderReplicatedExtension/modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)). Set the value for this key to an integer in the range `1` to `128`.

## See Also

- [NSExtensionFileProviderActions](information-property-list/nsextension/nsextensionfileprovideractions.md)
  The custom actions for a File Provider extension.
- [NSExtensionFileProviderDocumentGroup](information-property-list/nsextension/nsextensionfileproviderdocumentgroup.md)
  The identifier of a shared container that can be accessed by a Document Picker extension and its associated File Provider extension.
- [NSExtensionFileProviderSupportsEnumeration](information-property-list/nsextension/nsextensionfileprovidersupportsenumeration.md)
  A Boolean value that indicates whether a File Provider extension enumerates its content.
- [NSExtensionFileProviderDownloadPipelineDepth](information-property-list/nsextension/nsextensionfileproviderdownloadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to fetch data from remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionfileprovideruploadpipelinedepth)*