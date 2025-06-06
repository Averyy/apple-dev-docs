# noteNewRecentDocument(_:)

**Framework**: AppKit  
**Kind**: method

Adds or replaces an Open Recent menu item corresponding to the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteNewRecentDocument(_ document: NSDocument)
```

#### Discussion

This method constructs a URL and calls [`noteNewRecentDocumentURL(_:)`](nsdocumentcontroller/notenewrecentdocumenturl(_:).md). Subclasses might override this method to prevent certain documents or kinds of documents from getting into the list.

## Parameters

- `document`: The document to evaluate.

## See Also

- [var maximumRecentDocumentCount: Int](nsdocumentcontroller/maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](nsdocumentcontroller/clearrecentdocuments(_:).md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](nsdocumentcontroller/notenewrecentdocumenturl(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [var recentDocumentURLs: [URL]](nsdocumentcontroller/recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/notenewrecentdocument(_:))*