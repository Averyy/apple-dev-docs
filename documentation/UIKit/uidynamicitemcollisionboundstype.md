# UIDynamicItemCollisionBoundsType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the shape of the item’s collision bounds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum UIDynamicItemCollisionBoundsType
```

```c
enum UIDynamicItemCollisionBoundsType : NSUInteger;
```

## Topics

### Constants
- [UIDynamicItemCollisionBoundsType.rectangle](./uidynamicitemcollisionboundstype/rectangle.md)
  Rectangular collision bounds.
- [UIDynamicItemCollisionBoundsType.ellipse](./uidynamicitemcollisionboundstype/ellipse.md)
  Elliptical collision bounds. The shape of the ellipse is determined by the width and height of the item’s [`bounds`](./uidynamicitem/bounds.md) property.
- [UIDynamicItemCollisionBoundsType.path](./uidynamicitemcollisionboundstype/path.md)
  Path-based collision bounds. For this type, the shape is a [`UIBezierPath`](./uibezierpath.md) object stored in the item’s [`collisionBoundingPath`](./uidynamicitem/collisionboundingpath.md) property. See the description of that property for information about how to configure the path itself.
### Initializers
- [init?(rawValue: UInt)](./uidynamicitemcollisionboundstype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype)*