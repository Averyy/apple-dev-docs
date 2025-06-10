# TCColliderType

**Framework**: Touch Controls  
**Kind**: enum

Defines the type of collider.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
enum TCColliderType
```

## Topics

### Enumeration Cases
- [TCColliderType.circle](tccollidertype/circle.md)
  A circular collider.
- [TCColliderType.leftSide](tccollidertype/leftside.md)
  A collider representing the left side of the touch controller.
- [TCColliderType.rect](tccollidertype/rect.md)
  A rectangular collider.
- [TCColliderType.rightSide](tccollidertype/rightside.md)
  A collider representing the right side of the touch controller.
### Initializers
- [init?(rawValue: Int)](tccollidertype/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](tccollidertype/equatable-implementations.md)
- [RawRepresentable Implementations](tccollidertype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol TCCollider](tccollider.md)
  A protocol defining the collider properties for a control.
- [class TCRectCollider](tcrectcollider.md)
  A rectangular collider.
- [class TCCircleCollider](tccirclecollider.md)
  A circular collider.
- [class TCRegionCollider](tcregioncollider.md)
  A collider that covers a specific region of the touch controller.
- [enum TCRegionColliderRegion](tcregioncolliderregion.md)
  Defines the region of the touch controller that the `TCRegionCollider` represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tccollidertype)*