# NSExtensionFileProviderUploadPipelineDepth

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The per-domain limit of concurrent calls that a file provider extension can make to upload data.

**Availability**:
- macOS 12.0+

## Details

- **Name**: `NSExtensionFileProviderUploadPipelineDepth`
- **Type**: integer

## Discussion

Use this value to set the limit of concurrent calls to methods like [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](../../../FileProvider/nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md) and [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](../../../FileProvider/nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md). Set the value for this key to an integer in the range `1` to `128`.

## See Also

### File Provider
- [NSExtensionFileProviderActions](./nsextensionfileprovideractions.md)
  The custom actions for a File Provider extension.
- [NSExtensionFileProviderDocumentGroup](./nsextensionfileproviderdocumentgroup.md)
  The identifier of a shared container that can be accessed by a Document Picker extension and its associated File Provider extension.
- [NSExtensionFileProviderSupportsEnumeration](./nsextensionfileprovidersupportsenumeration.md)
  A Boolean value that indicates whether a File Provider extension enumerates its content.
- [NSExtensionFileProviderDownloadPipelineDepth](./nsextensionfileproviderdownloadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to fetch data from remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionfileprovideruploadpipelinedepth)*