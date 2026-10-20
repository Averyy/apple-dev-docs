# clearRecentDocuments(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Empties the recent documents list for the application.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func clearRecentDocuments(_ sender: Any?)
```

```objc
- (void) clearRecentDocuments:(id) sender;
```

#### Discussion

This is the action for the Clear menu command, but it can be called directly if necessary.

## See Also

### Managing the Open Recent Menu
- [var maximumRecentDocumentCount: Int](./maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func noteNewRecentDocumentURL(URL)](./notenewrecentdocumenturl%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](./notenewrecentdocument%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](./recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/clearrecentdocuments(_:))*