# browseVersions(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens the Versions browser in the document’s main window.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
func browseVersions(_ sender: Any?)
```

```objc
- (void) browseDocumentVersions:(id) sender;
```

#### Discussion

This is the action of the Browse Saved Versions menu item in a document-based app.

## Parameters

- `sender`: The control sending the message.

## See Also

### Browsing Document Versions
- [var isBrowsingVersions: Bool](./isbrowsingversions.md)
  A Boolean value that indicates whether the document is currently displaying the Versions browser.
- [func stopBrowsingVersions(completionHandler: (() -> Void)?)](./stopbrowsingversions%28completionhandler%29.md)
  Dismiss the Versions browser for the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/browseversions(_:))*