# init(rect:cornerRadius:)

**Framework**: SpriteKit  
**Kind**: init

Creates a shape with a rectangular path that has rounded corners.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
convenience init(rect: CGRect, cornerRadius: CGFloat)
```

#### Return Value

A new shape node.

## Parameters

- `rect`: A rectangle, relative to the node’s origin.
- `cornerRadius`: The radius of the rounded corners. The radius should not be a negative number. The value should be no larger than half of the rectangle’s width or height, whichever is smaller.

## See Also

- [convenience init(rect: CGRect)](skshapenode/init(rect:).md)
  Creates a shape node with a rectangular path.
- [convenience init(rectOf: CGSize)](skshapenode/init(rectof:).md)
  Creates a shape node with a rectangular path centered on the node’s origin.
- [convenience init(rectOf: CGSize, cornerRadius: CGFloat)](skshapenode/init(rectof:cornerradius:).md)
  Creates a shape with a rectangular path that has rounded corners centered on the node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/init(rect:cornerradius:))*