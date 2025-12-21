# isBrowsingVersions

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document is currently displaying the Versions browser.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
var isBrowsingVersions: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the versions browser is visible.

## See Also

- [func browseVersions(Any?)](nsdocument/browseversions(_:).md)
  Opens the Versions browser in the document’s main window.
- [func stopBrowsingVersions(completionHandler: (() -> Void)?)](nsdocument/stopbrowsingversions(completionhandler:).md)
  Dismiss the Versions browser for the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isbrowsingversions)*