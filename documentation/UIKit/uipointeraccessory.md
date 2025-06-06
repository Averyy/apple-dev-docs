# UIPointerAccessory

**Framework**: UIKit  
**Kind**: class

Constants that describe accessories to display alongside the primary pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerAccessory
```

## Topics

### Creating a pointer accessory
- [convenience init(UIPointerShape, position: UIPointerAccessory.Position)](uipointeraccessory/init(_:position:).md)
  Creates a pointer accessory with the specified shape and position.
- [class func arrow(UIPointerAccessory.Position) -> Self](uipointeraccessory/arrow(_:).md)
  Creates a pointer accessory with an arrow shape at the specified position.
### Matching the angle
- [var orientationMatchesAngle: Bool](uipointeraccessory/orientationmatchesangle.md)
  A Boolean value that indicates whether the system rotates the accessory to match its angle.
### Getting the shape
- [var shape: UIPointerShape](uipointeraccessory/shape-8pp0a.md)
  The shape of the accessory.
### Getting the position
- [var position: __UIPointerAccessoryPosition](uipointeraccessory/position-swift.property.md)
  The position of the accessory relative to the primary pointer.
- [UIPointerAccessory.Position](uipointeraccessory/position-swift.struct.md)
  A structure that specifies the position of the accessory relative to the primary pointer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPointerStyle](uipointerstyle.md)
  An object that defines the pointer shape and effect.
- [enum UIPointerShape](uipointershape-swift.enum.md)
  An object that defines the shape of custom pointers.
- [enum UIPointerEffect](uipointereffect-swift.enum.md)
  An effect that alters a view’s appearance when a pointer enters the current region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory)*