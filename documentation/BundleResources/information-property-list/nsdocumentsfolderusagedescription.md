# NSDocumentsFolderUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

**Availability**:
- macOS 10.15+

#### Discussion

The user implicitly grants your app access to a file in the Documents folder when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file in the Documents folder, the app can access that file without user consent.

The first time your app tries to access a file in the user’s Documents folder without implied user consent, the system prompts the user for permission to access the folder’s contents. Add the [`NSDocumentsFolderUsageDescription`](information-property-list/nsdocumentsfolderusagedescription.md) key to your app’s [`Information Property List`](information-property-list.md) file to provide a message that explains why your app needs access. The usage description is optional, but highly recommended.

App Sandbox enforces stricter limits on Documents folder access, so that policy may supersede this one if your app enables sandboxing. See [`App Sandbox`](https://developer.apple.com/documentation/Security/app-sandbox) for more information.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the `tccutil` command line utility with your app’s bundle ID:

```sh
$ tccutil reset SystemPolicyDocumentsFolder <bundleID>
```

## See Also

- [NSDesktopFolderUsageDescription](information-property-list/nsdesktopfolderusagedescription.md)
  A message that tells people why the app needs access to their Desktop folder.
- [NSDownloadsFolderUsageDescription](information-property-list/nsdownloadsfolderusagedescription.md)
  A message that tells people why the app needs access to the user’s Downloads folder.
- [NSNetworkVolumesUsageDescription](information-property-list/nsnetworkvolumesusagedescription.md)
  A message that tells people why the app needs access to files on a network volume.
- [NSRemovableVolumesUsageDescription](information-property-list/nsremovablevolumesusagedescription.md)
  A message that tells people why the app needs access to files on a removable volume.
- [NSFileProviderDomainUsageDescription](information-property-list/nsfileproviderdomainusagedescription.md)
  A message that tells people why the app needs access to files managed by a file provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdocumentsfolderusagedescription)*