# recentDocumentURLs

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The list of recent-document URLs.

**Availability**:
- macOS

## Declaration

```swift
var recentDocumentURLs: [URL] { get }
```

```objc
@property (copy, readonly) NSArray<NSURL *> * recentDocumentURLs;
```

#### Discussion

This property contains an array of [`NSURL`](../../Foundation/nsurl.md) objects corresponding to the recently opened documents. Do not override this property.

## See Also

### Managing the Open Recent Menu
- [var maximumRecentDocumentCount: Int](./maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](./clearrecentdocuments%28_%29.md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](./notenewrecentdocumenturl%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](./notenewrecentdocument%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/recentdocumenturls)*