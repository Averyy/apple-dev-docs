# UINavigationBarAppearance

**Framework**: UIKit  
**Kind**: class

An object for customizing the appearance of a navigation bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UINavigationBarAppearance
```

#### Overview

After creating a [`UINavigationBarAppearance`](uinavigationbarappearance.md) object, use the methods and properties of this class to specify the appearance you want for items in the navigation bar. Use the inherited properties from [`UIBarAppearance`](uibarappearance.md) to configure the background and shadow attributes of the navigation bar itself.

## Topics

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]](uinavigationbarappearance/titletextattributes.md)
  String attributes to apply to the text of a standard-size title.
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]](uinavigationbarappearance/largetitletextattributes.md)
  String attributes to apply to the text of a large-size title.
- [var titlePositionAdjustment: UIOffset](uinavigationbarappearance/titlepositionadjustment.md)
  The distance, in points, by which to offset the title horizontally and vertically.
### Configuring bar button items
- [var buttonAppearance: UIBarButtonItemAppearance](uinavigationbarappearance/buttonappearance.md)
  The appearance attributes for plain bar button items in the navigation bar.
### Configuring the Back button
- [var backButtonAppearance: UIBarButtonItemAppearance](uinavigationbarappearance/backbuttonappearance.md)
  The appearance attributes for the back button.
- [var backIndicatorImage: UIImage](uinavigationbarappearance/backindicatorimage.md)
  The image to display on the leading edge of the back button.
- [var backIndicatorTransitionMaskImage: UIImage](uinavigationbarappearance/backindicatortransitionmaskimage.md)
  The image for masking content flowing under the back indicator image during push and pop transitions.
- [func setBackIndicatorImage(UIImage?, transitionMaskImage: UIImage?)](uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:).md)
  Sets the back button indicator image and its transition mask.
### Configuring the Done button
- [var doneButtonAppearance: UIBarButtonItemAppearance](uinavigationbarappearance/donebuttonappearance.md)
  The appearance attributes for Done buttons.

## Relationships

### Inherits From
- [UIBarAppearance](uibarappearance.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance)*