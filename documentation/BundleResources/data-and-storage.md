# Data and storage

**Framework**: Bundle Resources

Regulate documents, URLs, and other kinds of data movement and storage.

#### Overview

The system needs to know what kinds of data your app stores, provides, or consumes. Add keys to your app’s [`Information Property List`](information-property-list.md) that declare your app’s data management capabilities.

## Topics

### Documents
- [CFBundleDocumentTypes](information-property-list/cfbundledocumenttypes.md)
  The document types supported by the bundle.
- [UISupportsDocumentBrowser](information-property-list/uisupportsdocumentbrowser.md)
  A Boolean value indicating whether the app is a document-based app.
- [LSSupportsOpeningDocumentsInPlace](information-property-list/lssupportsopeningdocumentsinplace.md)
  A Boolean value indicating whether the app may open the original document from a file provider, rather than a copy of the document.
- [NSDownloadsUbiquitousContents](information-property-list/nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.
### URL schemes
- [CFBundleURLTypes](information-property-list/cfbundleurltypes.md)
  A list of URL schemes (http, ftp, and so on) supported by the app.
### Universal type identifiers
- [UTExportedTypeDeclarations](information-property-list/utexportedtypedeclarations.md)
  The uniform type identifiers owned and exported by the app.
- [UTImportedTypeDeclarations](information-property-list/utimportedtypedeclarations.md)
  The uniform type identifiers inherently supported, but not owned, by the app.
### Network
- [NSAdvertisingAttributionReportEndpoint](information-property-list/nsadvertisingattributionreportendpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.
- [NSAppTransportSecurity](information-property-list/nsapptransportsecurity.md)
  A description of changes made to the default security for HTTP connections.
- [NSBonjourServices](information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [CKSharingSupported](information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.
### Background downloads
- [BAUsesAppleHosting](information-property-list/bausesapplehosting.md)
  A Boolean value that indicates whether you use Apple’s service to host your asset packs.
- [BAHasManagedAssetPacks](information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.
- [BAAppGroupID](information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAInitialDownloadRestrictions](information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAMaxInstallSize](information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAManifestURL](information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAEssentialMaxInstallSize](information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
### Storage
- [APFiles](information-property-list/apfiles.md)
  Describes the files or directories the app installs on the system.
- [APInstallerURL](information-property-list/apinstallerurl.md)
  The base path to the files or folders that the app installs.
- [NSSupportsPurgeableLocalStorage](information-property-list/nssupportspurgeablelocalstorage.md)
  A Boolean value indicating whether the app continues working if the system purges the local storage.
- [LSFileQuarantineEnabled](information-property-list/lsfilequarantineenabled.md)
  A Boolean value indicating whether the files this app creates are quarantined by default.
- [UIFileSharingEnabled](information-property-list/uifilesharingenabled.md)
  A Boolean value indicating whether the app shares files.
- [CSResourcesFileMapped](information-property-list/csresourcesfilemapped.md)
  A Boolean value indicating whether the app’s resources files should be mapped into memory.
- [NSDownloadsUbiquitousContents](information-property-list/nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.
### CoreML models
- [LSBundleContainsCoreMLmlmodelc](information-property-list/lsbundlecontainscoremlmlmodelc.md)
  A Boolean value indicating whether the app contains a Core ML model to optimize loading the model.
### Java
- [NSJavaRoot](information-property-list/nsjavaroot.md)
  The root directory for the app’s Java class files.

## See Also

- [Protected resources](protected-resources.md)
  Control an app’s access to protected system services and user data.
- [App services](app-services.md)
  Configure services provided by the app, like support for giving directions or using game controllers.
- [Kernel and drivers](kernel-and-drivers.md)
  Configure device drivers provided by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/data-and-storage)*