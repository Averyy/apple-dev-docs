# UIPointerStyle

**Framework**: UIKit  
**Kind**: class

An object that defines the pointer shape and effect.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerStyle
```

#### Overview

Whenever possible, match pointer styles to UIKit styles and make them consistent with the visual intent of similar views.

> **Note**:  When supporting the use of Apple Pencil, effect-based styles, such as a pointer style created using [`init(effect:shape:)`](uipointerstyle/init(effect:shape:).md) are fully supported, but shape-based pointer styles created using [`init(shape:constrainedAxes:)`](uipointerstyle/init(shape:constrainedaxes:).md) aren’t.

For more information, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/).

## Topics

### Creating a pointer style
- [convenience init(effect: UIPointerEffect, shape: UIPointerShape?)](uipointerstyle/init(effect:shape:).md)
  Applies the provided content effect and pointer shape to the current region.
- [convenience init(shape: UIPointerShape, constrainedAxes: UIAxis)](uipointerstyle/init(shape:constrainedaxes:).md)
  Morphs the pointer into the provided shape when hovering over the current region.
- [class func hidden() -> Self](uipointerstyle/hidden.md)
  Hides the pointer when it moves over the current region.
- [class func system() -> Self](uipointerstyle/system.md)
  Morphs the pointer into a default system-style pointer.
### Specifying pointer accessories
- [var accessories: [UIPointerAccessory]](uipointerstyle/accessories.md)
  Accessories to display alongside the pointer.
- [class UIPointerAccessory](uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.

## Relationships

### Inherits From
- [UIHoverStyle](uihoverstyle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum UIPointerShape](uipointershape-swift.enum.md)
  An object that defines the shape of custom pointers.
- [enum UIPointerEffect](uipointereffect-swift.enum.md)
  An effect that alters a view’s appearance when a pointer enters the current region.
- [class UIPointerAccessory](uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle)*