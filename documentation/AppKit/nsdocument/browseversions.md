# browseVersions(_:)

**Framework**: AppKit  
**Kind**: method

Opens the Versions browser in the document’s main window.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func browseVersions(_ sender: Any?)
```

#### Discussion

This is the action of the Browse Saved Versions menu item in a document-based app.

## Parameters

- `sender`: The control sending the message.

## See Also

- [var isBrowsingVersions: Bool](nsdocument/isbrowsingversions.md)
  A Boolean value that indicates whether the document is currently displaying the Versions browser.
- [func stopBrowsingVersions(completionHandler: (() -> Void)?)](nsdocument/stopbrowsingversions(completionhandler:).md)
  Dismiss the Versions browser for the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/browseversions(_:))*