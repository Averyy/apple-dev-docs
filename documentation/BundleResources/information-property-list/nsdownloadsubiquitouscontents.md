# NSDownloadsUbiquitousContents

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the system should download documents before handing them over to the app.

**Availability**:
- macOS 11.0+

## Details

- **Name**: `NSDownloadsUbiquitousContents`
- **Type**: boolean



**Default**: `NO`

## Discussion

By default, the system displays the download progress. Set the value to `YES` if you want your app to display a custom download progress indicator instead.

## See Also

### Documents
- [CFBundleDocumentTypes](./cfbundledocumenttypes.md)
  The document types supported by the bundle.
- [UISupportsDocumentBrowser](./uisupportsdocumentbrowser.md)
  A Boolean value indicating whether the app is a document-based app.
- [LSSupportsOpeningDocumentsInPlace](./lssupportsopeningdocumentsinplace.md)
  A Boolean value indicating whether the app may open the original document from a file provider, rather than a copy of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdownloadsubiquitouscontents)*