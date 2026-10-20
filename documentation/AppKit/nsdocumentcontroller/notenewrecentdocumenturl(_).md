# noteNewRecentDocumentURL(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds or replaces an Open Recent menu item corresponding to the data located by the URL.

**Availability**:
- macOS

## Declaration

```swift
func noteNewRecentDocumentURL(_ url: URL)
```

```objc
- (void) noteNewRecentDocumentURL:(NSURL *) url;
```

#### Discussion

`NSDocument` automatically calls this method when appropriate for `NSDocument`-based applications. Applications not based on `NSDocument` must also implement the [`application(_:openFile:)`](../nsapplicationdelegate/application%28_,openfile%29.md) method in the application delegate to handle requests from the Open Recent menu command. You can override this method in an `NSDocument`-based application to prevent certain kinds of documents from getting into the list (but you have to identify them by URL).

## Parameters

- `url`: The URL to evaluate.

## See Also

### Managing the Open Recent Menu
- [var maximumRecentDocumentCount: Int](./maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](./clearrecentdocuments%28_%29.md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocument(NSDocument)](./notenewrecentdocument%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](./recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/notenewrecentdocumenturl(_:))*