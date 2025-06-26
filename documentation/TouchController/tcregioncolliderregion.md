# TCRegionColliderRegion

**Framework**: Touch Controller  
**Kind**: enum

Defines the region of the touch controller that the `TCRegionCollider` represents.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum TCRegionColliderRegion
```

## Topics

### Getting the collider region
- [TCRegionColliderRegion.leftSide](tcregioncolliderregion/leftside.md)
  The left side of the touch controller.
- [TCRegionColliderRegion.rightSide](tcregioncolliderregion/rightside.md)
  The right side of the touch controller.
### Creating a collider region
- [init?(rawValue: Int)](tcregioncolliderregion/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](tcregioncolliderregion/equatable-implementations.md)
- [RawRepresentable Implementations](tcregioncolliderregion/rawrepresentable-implementations.md)

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
- [enum TCColliderType](tccollidertype.md)
  Defines the type of collider.
- [class TCRectCollider](tcrectcollider.md)
  A rectangular collider.
- [class TCCircleCollider](tccirclecollider.md)
  A circular collider.
- [class TCRegionCollider](tcregioncollider.md)
  A collider that covers a specific region of the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcregioncolliderregion)*