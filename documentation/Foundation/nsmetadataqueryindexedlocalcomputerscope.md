# NSMetadataQueryIndexedLocalComputerScope

**Framework**: Foundation  
**Kind**: var

Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).

**Availability**:
- macOS 10.9+

## Declaration

```swift
let NSMetadataQueryIndexedLocalComputerScope: String
```

## See Also

- [let NSMetadataQueryUserHomeScope: String](nsmetadataqueryuserhomescope.md)
  Search the user’s home directory.
- [let NSMetadataQueryLocalComputerScope: String](nsmetadataquerylocalcomputerscope.md)
  Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [let NSMetadataQueryNetworkScope: String](nsmetadataquerynetworkscope.md)
  Search all user-mounted remote volumes.
- [let NSMetadataQueryUbiquitousDocumentsScope: String](nsmetadataqueryubiquitousdocumentsscope.md)
  Search all files in the `Documents` directories of the app’s iCloud container directories.
- [let NSMetadataQueryUbiquitousDataScope: String](nsmetadataqueryubiquitousdatascope.md)
  Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: String](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md)
  Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [`NSMetadataItemURLKey`](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [`Security-Scoped URLs`](nsurl#Security-Scoped-URLs.md) in [`NSURL`](nsurl.md).
- [let NSMetadataQueryIndexedNetworkScope: String](nsmetadataqueryindexednetworkscope.md)
  Search all indexed user-mounted remote volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryindexedlocalcomputerscope)*