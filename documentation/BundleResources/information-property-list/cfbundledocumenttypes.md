# CFBundleDocumentTypes

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The document types supported by the bundle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Details

- **Name**: `CFBundleDocumentTypes` (Document types)
- **Type**: array of dictionary 

## Topics

### Property List Keys
- [CFBundleTypeIconFile](./cfbundledocumenttypes/cfbundletypeiconfile.md)
  The icon to associate with the document type.
- [CFBundleTypeName](./cfbundledocumenttypes/cfbundletypename.md)
  The abstract name for the document type.
- [CFBundleTypeRole](./cfbundledocumenttypes/cfbundletyperole.md)
  The app’s role with respect to the document type.
- [LSHandlerRank](./cfbundledocumenttypes/lshandlerrank.md)
  The ranking of this app among apps that declare themselves as editors or viewers of the given file type.
- [LSItemContentTypes](./cfbundledocumenttypes/lsitemcontenttypes.md)
  The document file types the app supports.
- [LSTypeIsPackage](./cfbundledocumenttypes/lstypeispackage.md)
  A Boolean value indicating whether the document is distributed as a bundle.
- [NSDocumentClass](./cfbundledocumenttypes/nsdocumentclass.md)
  The subclass used to create instances of this document.
- [NSExportableTypes](./cfbundledocumenttypes/nsexportabletypes.md)
  The file types that this document can be exported to.

## See Also

### Documents
- [UISupportsDocumentBrowser](./uisupportsdocumentbrowser.md)
  A Boolean value indicating whether the app is a document-based app.
- [LSSupportsOpeningDocumentsInPlace](./lssupportsopeningdocumentsinplace.md)
  A Boolean value indicating whether the app may open the original document from a file provider, rather than a copy of the document.
- [NSDownloadsUbiquitousContents](./nsdownloadsubiquitouscontents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundledocumenttypes)*