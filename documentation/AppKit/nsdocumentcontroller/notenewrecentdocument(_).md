# noteNewRecentDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds or replaces an Open Recent menu item corresponding to the document.

**Availability**:
- macOS

## Declaration

```swift
func noteNewRecentDocument(_ document: NSDocument)
```

```objc
- (void) noteNewRecentDocument:(NSDocument *) document;
```

## Discussion

This method constructs a URL and calls [`noteNewRecentDocumentURL(_:)`](./notenewrecentdocumenturl%28_%29.md). Subclasses might override this method to prevent certain documents or kinds of documents from getting into the list.

## Parameters

- `document`: The document to evaluate.

## See Also

### Managing the Open Recent Menu
- [var maximumRecentDocumentCount: Int](./maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](./clearrecentdocuments%28_%29.md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](./notenewrecentdocumenturl%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [var recentDocumentURLs: [URL]](./recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/notenewrecentdocument(_:))*