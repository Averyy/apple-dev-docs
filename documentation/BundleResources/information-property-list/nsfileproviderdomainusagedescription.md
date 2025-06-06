# NSFileProviderDomainUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells the user why the app needs access to files managed by a file provider.

**Availability**:
- macOS 10.15+

#### Discussion

The user implicitly grants your app access to a file managed by a file provider when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file managed by a file provider, the app can access that file without user consent.

The first time your app tries to access a file managed by a file provider without implied user consent, the system prompts the user for permission. Add the [`NSFileProviderDomainUsageDescription`](information-property-list/nsfileproviderdomainusagedescription.md) key to your app’s [`Information Property List`](information-property-list.md) file to provide a string for the prompt that explains why your app needs access. The usage description is optional, but highly recommended.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the `tccutil` command line utility with your app’s bundle ID:

```sh
$ tccutil reset FileProviderDomain <bundleID>
```

## See Also

- [NSDesktopFolderUsageDescription](information-property-list/nsdesktopfolderusagedescription.md)
  A message that tells the user why the app needs access to the user’s Desktop folder.
- [NSDocumentsFolderUsageDescription](information-property-list/nsdocumentsfolderusagedescription.md)
  A message that tells the user why the app needs access to the user’s Documents folder.
- [NSDownloadsFolderUsageDescription](information-property-list/nsdownloadsfolderusagedescription.md)
  A message that tells the user why the app needs access to the user’s Downloads folder.
- [NSNetworkVolumesUsageDescription](information-property-list/nsnetworkvolumesusagedescription.md)
  A message that tells the user why the app needs access to files on a network volume.
- [NSRemovableVolumesUsageDescription](information-property-list/nsremovablevolumesusagedescription.md)
  A message that tells the user why the app needs access to files on a removable volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfileproviderdomainusagedescription)*