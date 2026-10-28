# findIndicatorNeedsUpdate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Invoke to specify that the find indicator needs updating when not contained within a scroll view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var findIndicatorNeedsUpdate: Bool { get set }
```

```objc
@property BOOL findIndicatorNeedsUpdate;
```

## Discussion

If the [`client`](./client.md) object’s document is not scrolled by an instance of `NSScrollView`, then set this property to [`true`](../../Swift/true.md) when scrolling occurs to cause the find indicator to be updated appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/findindicatorneedsupdate)*