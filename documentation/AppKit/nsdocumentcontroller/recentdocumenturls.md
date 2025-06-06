# recentDocumentURLs

**Framework**: AppKit  
**Kind**: property

The list of recent-document URLs.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var recentDocumentURLs: [URL] { get }
```

#### Discussion

This property contains an array of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects corresponding to the recently opened documents. Do not override this property.

## See Also

- [var maximumRecentDocumentCount: Int](nsdocumentcontroller/maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](nsdocumentcontroller/clearrecentdocuments(_:).md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](nsdocumentcontroller/notenewrecentdocumenturl(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](nsdocumentcontroller/notenewrecentdocument(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/recentdocumenturls)*