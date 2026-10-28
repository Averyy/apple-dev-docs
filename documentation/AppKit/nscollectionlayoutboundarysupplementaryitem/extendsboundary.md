# extendsBoundary

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a boundary supplementary item extends the content area of the section or layout it’s attached to.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var extendsBoundary: Bool { get set }
```

```objc
@property BOOL extendsBoundary;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Specifying position
- [var offset: NSPoint](./offset.md)
  The floating-point value of the boundary supplementary item’s offset from the section or layout it’s attached to.
- [var alignment: NSRectAlignment](./alignment.md)
  The alignment of the boundary supplementary item relative to the section or layout it’s attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutboundarysupplementaryitem/extendsboundary)*