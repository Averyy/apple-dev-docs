# UIFileSharingEnabled

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app shares files.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Details

- **Name**: `UIFileSharingEnabled` (Application supports iTunes file sharing)
- **Type**: boolean

#### Discussion

If you set this key to `YES`, your app can share files with the user. Place the files in a `Documents` folder located in the app’s home directiory. The default value is `NO`.

## See Also

### Related Documentation
- [LSSupportsOpeningDocumentsInPlace](./lssupportsopeningdocumentsinplace.md)
  A Boolean value indicating whether the app may open the original document from a file provider, rather than a copy of the document.
- [func NSHomeDirectory() -> String](../../Foundation/nshomedirectory%28%29.md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
### Storage
- [APFiles](./apfiles.md)
  Describes the files or directories the app installs on the system.
- [APInstallerURL](./apinstallerurl.md)
  The base path to the files or folders that the app installs.
- [NSSupportsPurgeableLocalStorage](./nssupportspurgeablelocalstorage.md)
  A Boolean value indicating whether the app continues working if the system purges the local storage.
- [LSFileQuarantineEnabled](./lsfilequarantineenabled.md)
  A Boolean value indicating whether the files this app creates are quarantined by default.
- [CSResourcesFileMapped](./csresourcesfilemapped.md)
  A Boolean value indicating whether the app’s resources files should be mapped into memory.
- [NSDownloadsUbiquitousContents](./nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uifilesharingenabled)*