# totalBounds

**Framework**: AppKit  
**Kind**: property

The most recent bounding rectangle that the system used to draw the string.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var totalBounds: CGRect { get }
```

#### Discussion

This property contains the bounding rectangle that was last used when calling the [`draw(with:options:context:)`](https://developer.apple.com/documentation/foundation/nsattributedstring/1524971-draw) method. The rectangle is specified in the coordinate system of the drawn string. (The origin of the bounds corresponds to neither a view the string might have been drawn into nor the origin of a possible [`draw(in:)`](https://developer.apple.com/documentation/foundation/nsattributedstring/1531631-draw) call.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext/totalbounds)*