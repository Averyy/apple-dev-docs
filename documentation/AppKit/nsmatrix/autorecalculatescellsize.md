# autorecalculatesCellSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the matrix auto-recalculates its cell size.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var autorecalculatesCellSize: Bool { get set }
```

```objc
@property BOOL autorecalculatesCellSize;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), auto-recalculation occurs. The matrix will adjust its [`cellSize`](./cellsize.md) to accommodate its largest cell. Changing the `cellSize` does not directly affect the frame of the matrix; however it does affect the intrinsic content size, which may cause the receiver to resize under Auto Layout. When using Auto Layout, you typically want this to be set to [`true`](../../Swift/true.md).

The default value of this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/autorecalculatescellsize)*