# extendsBoundary

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a boundary supplementary item extends the content area of the section or layout it’s attached to.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var extendsBoundary: Bool { get set }
```

```objc
@property (nonatomic) BOOL extendsBoundary;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Specifying position
- [var offset: CGPoint](./offset.md)
  The floating-point value of the boundary supplementary item’s offset from the section or layout it’s attached to.
- [var alignment: NSRectAlignment](./alignment.md)
  The alignment of the boundary supplementary item relative to the section or layout it’s attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutboundarysupplementaryitem/extendsboundary)*