# ARPlaneAnchor.Alignment

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The kinds of alignment — horizontal or vertical — that a plane anchor can have.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
enum Alignment
```

```c
enum ARPlaneAnchorAlignment : NSInteger;
```

## Topics

### Alignment Values
- [ARPlaneAnchor.Alignment.horizontal](./alignment-swift.enum/horizontal.md)
  The plane is perpendicular to gravity.
- [ARPlaneAnchor.Alignment.vertical](./alignment-swift.enum/vertical.md)
  The plane is parallel to gravity.
### Initializers
- [init?(rawValue: Int)](./alignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Orientation
- [var alignment: ARPlaneAnchor.Alignment](./alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/alignment-swift.enum)*