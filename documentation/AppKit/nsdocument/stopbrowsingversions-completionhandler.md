# stopBrowsingVersions(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Dismiss the Versions browser for the current document.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func stopBrowsingVersions() async
```

#### Discussion

## Parameters

- `completionHandler`: The completion handler block to call when the Versions browser is fully dismissed. AppKit calls this block on your app’s main thread, waiting for any dismissal animations to complete before calling it. The block block has no return value and no parameters.

## See Also

- [func browseVersions(Any?)](nsdocument/browseversions(_:).md)
  Opens the Versions browser in the document’s main window.
- [var isBrowsingVersions: Bool](nsdocument/isbrowsingversions.md)
  A Boolean value that indicates whether the document is currently displaying the Versions browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/stopbrowsingversions(completionhandler:))*