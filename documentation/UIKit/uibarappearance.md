# UIBarAppearance

**Framework**: UIKit  
**Kind**: class

An object for customizing the basic appearance of system bars.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarAppearance
```

#### Overview

A [`UIBarAppearance`](uibarappearance.md) object contains the common traits shared by navigation bars, tab bars, and toolbars. When configuring a specific type of bar, you usually instantiate the appropriate bar appearance subclass. However, you may also create a [`UIBarAppearance`](uibarappearance.md) object, configure its properties, and use it to create new bar appearance objects in your app.

## Topics

### Creating a custom bar appearance object
- [init(idiom: UIUserInterfaceIdiom)](uibarappearance/init(idiom:).md)
  Creates a new bar appearance object that targets the specified idiom.
- [init(barAppearance: UIBarAppearance)](uibarappearance/init(barappearance:).md)
  Creates a new bar appearance object by copying relevant data from the specified appearance object.
- [convenience init()](uibarappearance/init.md)
  Creates a new bar appearance object containing default values.
- [init(coder: NSCoder)](uibarappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.
### Copying a custom bar appearance object
- [func copy() -> Self](uibarappearance/copy.md)
  Creates a copy of the appearance object.
### Resetting the appearance properties
- [func configureWithDefaultBackground()](uibarappearance/configurewithdefaultbackground.md)
  Configures the bar appearance object with default background and shadow values.
- [func configureWithOpaqueBackground()](uibarappearance/configurewithopaquebackground.md)
  Configures the bar appearance object with a set of opaque colors that are appropriate for the current theme.
- [func configureWithTransparentBackground()](uibarappearance/configurewithtransparentbackground.md)
  Configures the bar appearance object with a transparent background and no shadow.
### Configuring the background appearance
- [var backgroundEffect: UIBlurEffect?](uibarappearance/backgroundeffect.md)
  The blur effect to apply to the bar’s background.
- [var backgroundColor: UIColor?](uibarappearance/backgroundcolor.md)
  The background color of the bar.
- [var backgroundImage: UIImage?](uibarappearance/backgroundimage.md)
  The image to display on top of the bar’s background color.
- [var backgroundImageContentMode: UIView.ContentMode](uibarappearance/backgroundimagecontentmode.md)
  The content mode to use when displaying the bar’s background image.
### Configuring the shadow appearance
- [var shadowColor: UIColor?](uibarappearance/shadowcolor.md)
  The color to apply to the bar’s custom or default shadow.
- [var shadowImage: UIImage?](uibarappearance/shadowimage.md)
  The image to use for the bar’s shadow.
### Getting the supported idiom
- [var idiom: UIUserInterfaceIdiom](uibarappearance/idiom.md)
  The idiom targeted by this bar appearance object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UINavigationBarAppearance](uinavigationbarappearance.md)
- [UITabBarAppearance](uitabbarappearance.md)
- [UIToolbarAppearance](uitoolbarappearance.md)
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

## See Also

- [class UIBarButtonItemAppearance](uibarbuttonitemappearance.md)
  An object for customizing the appearance of bar button items.
- [class UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md)
  A data object containing the specific customizations for a bar button item in a particular state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance)*