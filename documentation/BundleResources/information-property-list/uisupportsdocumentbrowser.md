# UISupportsDocumentBrowser

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app is a document-based app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Details

- **Name**: `UISupportsDocumentBrowser` (Supports Document Browser)
- **Type**: boolean

## Discussion

To allow other apps to open and edit the files stored in your app’s `Documents` folder, set this key to `YES`. This key also lets users set the app’s default save location in Settings.

## See Also

### Related Documentation
- [Setting up a document browser app](../../UIKit/setting-up-a-document-browser-app.md)
  Add a document browser view controller to your app.
### Documents
- [CFBundleDocumentTypes](./cfbundledocumenttypes.md)
  The document types supported by the bundle.
- [LSSupportsOpeningDocumentsInPlace](./lssupportsopeningdocumentsinplace.md)
  A Boolean value indicating whether the app may open the original document from a file provider, rather than a copy of the document.
- [NSDownloadsUbiquitousContents](./nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportsdocumentbrowser)*