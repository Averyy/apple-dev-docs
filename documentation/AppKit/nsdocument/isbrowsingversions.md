# isBrowsingVersions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document is currently displaying the Versions browser.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var isBrowsingVersions: Bool { get }
```

```objc
@property (readonly, getter=isBrowsingVersions) BOOL browsingVersions;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the versions browser is visible.

## See Also

### Browsing Document Versions
- [func browseVersions(Any?)](./browseversions%28_%29.md)
  Opens the Versions browser in the document’s main window.
- [func stopBrowsingVersions(completionHandler: (() -> Void)?)](./stopbrowsingversions%28completionhandler%29.md)
  Dismiss the Versions browser for the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isbrowsingversions)*