# UIBarButtonItemStateAppearance

**Framework**: UIKit  
**Kind**: class

A data object containing the specific customizations for a bar button item in a particular state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarButtonItemStateAppearance
```

#### Overview

Use a [`UIBarButtonItemStateAppearance`](uibarbuttonitemstateappearance.md) object to customize the title and background image of your bar button items. Don’t create [`UIBarButtonItemStateAppearance`](uibarbuttonitemstateappearance.md) objects yourself. Instead, create a [`UIBarButtonItemAppearance`](uibarbuttonitemappearance.md) object and use its properties to fetch the appearance attributes for the button in a particular state. For example, to set the button’s attributes when it’s in the normal state, configure the object in the [`normal`](uibarbuttonitemappearance/normal.md) property.

## Topics

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]](uibarbuttonitemstateappearance/titletextattributes.md)
  String attributes to apply to the text of the bar button item’s title.
- [var titlePositionAdjustment: UIOffset](uibarbuttonitemstateappearance/titlepositionadjustment.md)
  The additional amount by which to offset the title horizontally and vertically.
### Configuring the background appearance
- [var backgroundImage: UIImage?](uibarbuttonitemstateappearance/backgroundimage.md)
  A background image to display around the button.
- [var backgroundImagePositionAdjustment: UIOffset](uibarbuttonitemstateappearance/backgroundimagepositionadjustment.md)
  The distance, in points, by which to offset the background image horizontally and vertically.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIBarAppearance](uibarappearance.md)
  An object for customizing the basic appearance of system bars.
- [class UIBarButtonItemAppearance](uibarbuttonitemappearance.md)
  An object for customizing the appearance of bar button items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemstateappearance)*