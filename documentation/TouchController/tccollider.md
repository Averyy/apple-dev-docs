# TCCollider

**Framework**: Touch Controller  
**Kind**: protocol

A protocol defining the collider properties for a control.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol TCCollider : NSObjectProtocol
```

## Topics

### Getting the type of collider
- [func colliderType() -> TCColliderType](tccollider/collidertype.md)
  The type of the collider.
### Check whether a collider contains a point
- [func contains(CGPoint) -> Bool](tccollider/contains(_:).md)
  Determines whether the collider contains the specified point.
### Configure the enabled state
- [func enabled() -> Bool](tccollider/enabled.md)
  A Boolean value that indicates whether the collider is enabled.
- [func setEnabled(Bool)](tccollider/setenabled(_:).md)
  Sets whether the collider is enabled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [TCCircleCollider](tccirclecollider.md)
- [TCRectCollider](tcrectcollider.md)
- [TCRegionCollider](tcregioncollider.md)

## See Also

- [enum TCColliderType](tccollidertype.md)
  Defines the type of collider.
- [class TCRectCollider](tcrectcollider.md)
  A rectangular collider.
- [class TCCircleCollider](tccirclecollider.md)
  A circular collider.
- [class TCRegionCollider](tcregioncollider.md)
  A collider that covers a specific region of the touch controller.
- [enum TCRegionColliderRegion](tcregioncolliderregion.md)
  Defines the region of the touch controller that the `TCRegionCollider` represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccollider)*