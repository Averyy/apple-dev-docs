# UIBarItem

**Framework**: UIKit  
**Kind**: class

An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarItem
```

#### Overview

Items on a bar behave in a way similar to buttons (instances of [`UIButton`](uibutton.md)). They have a title, image, action, and target. You can also enable and disable an item on a bar.

##### Customize Appearance

You can customize the image to represent the item, and the position of the image, using [`image`](uibaritem/image.md) and [`imageInsets`](uibaritem/imageinsets.md) respectively.

You can also specify a custom image and position to use in landscape orientation when using the iPhone appearance idiom using [`landscapeImagePhone`](uibaritem/landscapeimagephone.md) and [`landscapeImagePhoneInsets`](uibaritem/landscapeimagephoneinsets.md) respectively. In addition, you can customize the title’s text attributes using [`setTitleTextAttributes(_:for:)`](uibaritem/settitletextattributes(_:for:).md), either for a single item, or for all items by using the appearance proxy (for example, `[UIBarItem appearance]`).

## Topics

### Creating a bar item
- [init()](uibaritem/init.md)
  Initializes the bar item to its default state.
- [init?(coder: NSCoder)](uibaritem/init(coder:).md)
  Creates a bar item from data in an unarchiver.
### Getting and setting properties
- [var title: String?](uibaritem/title.md)
  The title displayed on the item.
- [var image: UIImage?](uibaritem/image.md)
  The image used to represent the item.
- [var landscapeImagePhone: UIImage?](uibaritem/landscapeimagephone.md)
  The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [var largeContentSizeImage: UIImage?](uibaritem/largecontentsizeimage.md)
  The image to display for users who are blind or have low vision.
- [var imageInsets: UIEdgeInsets](uibaritem/imageinsets.md)
  The image inset or outset for each edge.
- [var landscapeImagePhoneInsets: UIEdgeInsets](uibaritem/landscapeimagephoneinsets.md)
  The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [var largeContentSizeImageInsets: UIEdgeInsets](uibaritem/largecontentsizeimageinsets.md)
  The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [var isEnabled: Bool](uibaritem/isenabled.md)
  A Boolean value indicating whether the item is enabled.
- [var tag: Int](uibaritem/tag.md)
  The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.
### Customizing appearance
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uibaritem/settitletextattributes(_:for:).md)
  Sets the title’s text attributes for a given control state.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uibaritem/titletextattributes(for:).md)
  Returns the title’s text attributes for a given control state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIBarButtonItem](uibarbuttonitem.md)
- [UITabBarItem](uitabbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIAppearance](uiappearance.md)

## See Also

- [class UIBarButtonItem](uibarbuttonitem.md)
  A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.
- [class UIBarButtonItemGroup](uibarbuttonitemgroup.md)
  A group of one or more bar button items for placement on a navigation bar or shortcuts bar.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [class UIToolbar](uitoolbar.md)
  A control that displays one or more buttons along an edge of your interface.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [protocol UIBarPositioning](uibarpositioning.md)
  A set of methods for defining the positioning of bars in iOS apps.
- [protocol UIBarPositioningDelegate](uibarpositioningdelegate.md)
  A set of methods that support the positioning of a bar that conforms to the [`UIBarPositioning`](uibarpositioning.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem)*