# UIBarButtonItemGroup

**Framework**: UIKit  
**Kind**: class

A group of one or more bar button items for placement on a navigation bar or shortcuts bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarButtonItemGroup
```

#### Overview

A group contains one or more bar button items and an optional representative item that’s displayed instead of the individual items under space constraints. You can create any number of groups and configure each group with any number of items.

When creating a group with more than one bar button item, it’s recommended that you also provide a representative item to display. The representative item must be a completely separate bar button item; it must not be one of the items already in the group. UIKit displays the representative item when there isn’t enough room to display all of the group’s items in the bar. Taps in the representative item call that item’s action method. When you don’t specify an action method, UIKit automatically displays the items in the group using a standard interface. To present your own interface, provide a custom action method and use it to display the interface you want.

##### Support the Shortcuts Bar

After configuring a group, assign it to the [`UITextInputAssistantItem`](uitextinputassistantitem.md) object associated with one of your app’s responder objects. Your custom items are displayed only in conjunction with the system keyboard. When the keyboard is displayed, UIKit retrieves your custom groups from the text input assistant item and adds the corresponding items to the shortcuts bar. You may specify more than one group before and after the typing suggestions. UIKit tries to display as many items as possible on the shortcuts bar, falling back to the groups’ representative items as needed.

## Topics

### Creating a group
- [class func fixedGroup(representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/fixedgroup(representativeitem:items:).md)
  Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [class func movableGroup(customizationIdentifier: String, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/movablegroup(customizationidentifier:representativeitem:items:).md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [class func optionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/optionalgroup(customizationidentifier:isindefaultcustomization:representativeitem:items:).md)
  Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)](uibarbuttonitemgroup/init(barbuttonitems:representativeitem:).md)
  Creates a fixed group with the specified items.
- [init?(coder: NSCoder)](uibarbuttonitemgroup/init(coder:).md)
  Creates a bar button item group from data in an unarchiver.
### Configuring the group
- [var barButtonItems: [UIBarButtonItem]](uibarbuttonitemgroup/barbuttonitems.md)
  The bar button items to display on the bar.
- [var representativeItem: UIBarButtonItem?](uibarbuttonitemgroup/representativeitem.md)
  The item to display for a group when space is constrained.
- [var alwaysAvailable: Bool](uibarbuttonitemgroup/alwaysavailable.md)
  A Boolean value that determines whether the group is always available through the UI.
### Determining the group’s appearance
- [var isDisplayingRepresentativeItem: Bool](uibarbuttonitemgroup/isdisplayingrepresentativeitem.md)
  A Boolean value indicating whether the representative item is showing in place of the group’s items.
- [var isHidden: Bool](uibarbuttonitemgroup/ishidden.md)
  A Boolean that determines the visibility of the group.
### Representing the group in a menu
- [var menuRepresentation: UIMenuElement?](uibarbuttonitemgroup/menurepresentation.md)
  A menu element that represents the group when it appears in a menu.
### Type Methods
- [class func fixedSpace() -> UIBarButtonItemGroup](uibarbuttonitemgroup/fixedspace.md)
  Returns a new group that contains a single zero-width fixed space item inside it.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIBarItem](uibaritem.md)
  An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.
- [class UIBarButtonItem](uibarbuttonitem.md)
  A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [class UIToolbar](uitoolbar.md)
  A control that displays one or more buttons along the bottom edge of your interface.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [protocol UIBarPositioning](uibarpositioning.md)
  A set of methods for defining the positioning of bars in iOS apps.
- [protocol UIBarPositioningDelegate](uibarpositioningdelegate.md)
  A set of methods that support the positioning of a bar that conforms to the [`UIBarPositioning`](uibarpositioning.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup)*