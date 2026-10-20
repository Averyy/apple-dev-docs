# stopBrowsingVersions(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dismiss the Versions browser for the current document.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func stopBrowsingVersions(completionHandler: (() -> Void)? = nil)
```

```swift
func stopBrowsingVersions() async
```

```objc
- (void) stopBrowsingVersionsWithCompletionHandler:(void (^)()) completionHandler;
```

#### Discussion

## Parameters

- `completionHandler`: The completion handler block to call when the Versions browser is fully dismissed. AppKit calls this block on your app’s main thread, waiting for any dismissal animations to complete before calling it. The block block has no return value and no parameters.

## See Also

### Browsing Document Versions
- [func browseVersions(Any?)](./browseversions%28_%29.md)
  Opens the Versions browser in the document’s main window.
- [var isBrowsingVersions: Bool](./isbrowsingversions.md)
  A Boolean value that indicates whether the document is currently displaying the Versions browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/stopbrowsingversions(completionhandler:))*