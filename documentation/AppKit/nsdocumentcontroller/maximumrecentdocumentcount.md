# maximumRecentDocumentCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of items that may be presented in the standard Open Recent menu.

**Availability**:
- macOS

## Declaration

```swift
var maximumRecentDocumentCount: Int { get }
```

```objc
@property (readonly) NSUInteger maximumRecentDocumentCount;
```

#### Discussion

A value of 0 indicates that `NSDocumentController` will not attempt to add an Open Recent menu to your application’s File menu, although `NSDocumentController` will not attempt to remove any preexisting Open Recent menu item. The default implementation returns a value that is subject to change and may or may not be derived from a setting made by the user in System Preferences.

## See Also

### Managing the Open Recent Menu
- [func clearRecentDocuments(Any?)](./clearrecentdocuments%28_%29.md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](./notenewrecentdocumenturl%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](./notenewrecentdocument%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](./recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/maximumrecentdocumentcount)*