# TCRegionCollider

**Framework**: Touch Controller  
**Kind**: class

A collider that covers a specific region of the touch controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCRegionCollider
```

## Topics

### Creating a region collider
- [init(region: TCRegionColliderRegion, touchController: TCTouchController)](tcregioncollider/init(region:touchcontroller:).md)
  Creates a new region collider with the specified region and touch controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TCCollider](tccollider.md)

## See Also

- [protocol TCCollider](tccollider.md)
  A protocol defining the collider properties for a control.
- [enum TCColliderType](tccollidertype.md)
  Defines the type of collider.
- [class TCRectCollider](tcrectcollider.md)
  A rectangular collider.
- [class TCCircleCollider](tccirclecollider.md)
  A circular collider.
- [enum TCRegionColliderRegion](tcregioncolliderregion.md)
  Defines the region of the touch controller that the `TCRegionCollider` represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcregioncollider)*