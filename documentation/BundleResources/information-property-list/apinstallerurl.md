# APInstallerURL

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The base path to the files or folders that the app installs.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `APInstallerURL` (Installation directory base file URL)
- **Type**: string

#### Discussion

Use the format `file://localhost/path/` for the path.

## See Also

### Storage
- [APFiles](./apfiles.md)
  Describes the files or directories the app installs on the system.
- [NSSupportsPurgeableLocalStorage](./nssupportspurgeablelocalstorage.md)
  A Boolean value indicating whether the app continues working if the system purges the local storage.
- [LSFileQuarantineEnabled](./lsfilequarantineenabled.md)
  A Boolean value indicating whether the files this app creates are quarantined by default.
- [UIFileSharingEnabled](./uifilesharingenabled.md)
  A Boolean value indicating whether the app shares files.
- [CSResourcesFileMapped](./csresourcesfilemapped.md)
  A Boolean value indicating whether the app’s resources files should be mapped into memory.
- [NSDownloadsUbiquitousContents](./nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/apinstallerurl)*