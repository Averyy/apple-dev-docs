# autorecalculatesCellSize

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the matrix auto-recalculates its cell size.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var autorecalculatesCellSize: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), auto-recalculation occurs. The matrix will adjust its [`cellSize`](nsmatrix/cellsize.md) to accommodate its largest cell. Changing the `cellSize` does not directly affect the frame of the matrix; however it does affect the intrinsic content size, which may cause the receiver to resize under Auto Layout. When using Auto Layout, you typically want this to be set to [`true`](https://developer.apple.com/documentation/Swift/true).

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/autorecalculatescellsize)*