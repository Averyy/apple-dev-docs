# noteNewRecentDocumentURL(_:)

**Framework**: AppKit  
**Kind**: method

Adds or replaces an Open Recent menu item corresponding to the data located by the URL.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteNewRecentDocumentURL(_ url: URL)
```

#### Discussion

`NSDocument` automatically calls this method when appropriate for `NSDocument`-based applications. Applications not based on `NSDocument` must also implement the [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md) method in the application delegate to handle requests from the Open Recent menu command. You can override this method in an `NSDocument`-based application to prevent certain kinds of documents from getting into the list (but you have to identify them by URL).

## Parameters

- `url`: The URL to evaluate.

## See Also

- [var maximumRecentDocumentCount: Int](nsdocumentcontroller/maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](nsdocumentcontroller/clearrecentdocuments(_:).md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocument(NSDocument)](nsdocumentcontroller/notenewrecentdocument(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](nsdocumentcontroller/recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/notenewrecentdocumenturl(_:))*