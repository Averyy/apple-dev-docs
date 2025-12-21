# UIBarButtonItem

**Framework**: UIKit  
**Kind**: class

A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarButtonItem
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Overview

You typically use Interface Builder to create and configure bar button items. However, you can customize the appearance of buttons by sending the setter messages to [`UIBarButtonItemAppearance`](uibarbuttonitemappearance.md) to customize all buttons, or to a specific [`UIBarButtonItem`](uibarbuttonitem.md) instance. You can use customized buttons in standard places in a [`UINavigationItem`](uinavigationitem.md) object or a [`UIToolbar`](uitoolbar.md) instance.

In general, specify a value for the normal state so that other states without a custom value set can use it. Similarly, when a property depends on the bar metrics (for instance, on the iPhone in landscape orientation, bars have a different height from the standard), specify a value of [`UIBarMetrics.default`](uibarmetrics/default.md).

## Topics

### Creating items
- [convenience init(title: String?, image: UIImage?, primaryAction: UIAction?, menu: UIMenu?)](uibarbuttonitem/init(title:image:primaryaction:menu:).md)
  Creates a plain-style item using the specified title, image, primary action, and context menu.
- [convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu?)](uibarbuttonitem/init(title:image:target:action:menu:).md)
  Creates a plain-style item using the specified title, image, target, action, and context menu.
- [init()](uibarbuttonitem/init.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](uibarbuttonitem/init(coder:).md)
  Creates an item from data in an unarchiver.
### Creating items of a specific style
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(title:style:target:action:).md)
  Creates an item using the specified title, style, target, and action.
- [convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:style:target:action:).md)
  Creates an item using the specified image, style, target, and action.
- [convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](uibarbuttonitem/init(image:landscapeimagephone:style:target:action:).md)
  Creates an item using the specified images, style, target, and action.
### Creating system items
- [convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction?, menu: UIMenu?)](uibarbuttonitem/init(systemitem:primaryaction:menu:).md)
  Creates an item using the specified system item, primary action, and context menu.
- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](uibarbuttonitem/init(barbuttonsystemitem:target:action:).md)
  Creates an item using the specified system item, target, and action.
- [UIBarButtonItem.SystemItem](uibarbuttonitem/systemitem.md)
  Constants that define system-supplied images for bar button items.
### Creating custom items
- [convenience init(customView: UIView)](uibarbuttonitem/init(customview:).md)
  Creates an item using the specified custom view.
### Creating space items
- [class func fixedSpace(CGFloat) -> Self](uibarbuttonitem/fixedspace(_:).md)
  Creates a new fixed-width space item.
- [class func fixedSpace() -> Self](uibarbuttonitem/fixedspace.md)
  Creates a new fixed space item of zero width.
- [class func flexibleSpace() -> Self](uibarbuttonitem/flexiblespace.md)
  Creates a new flexible-width space item.
### Creating groups
- [func creatingOptionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool) -> UIBarButtonItemGroup](uibarbuttonitem/creatingoptionalgroup(customizationidentifier:isindefaultcustomization:).md)
  Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [func creatingFixedGroup() -> UIBarButtonItemGroup](uibarbuttonitem/creatingfixedgroup.md)
  Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [func creatingMovableGroup(customizationIdentifier: String) -> UIBarButtonItemGroup](uibarbuttonitem/creatingmovablegroup(customizationidentifier:).md)
  Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.
### Managing the custom view
- [var customView: UIView?](uibarbuttonitem/customview.md)
  A custom view representing the item.
### Managing the action
- [var primaryAction: UIAction?](uibarbuttonitem/primaryaction.md)
  The action associated with the item.
- [var changesSelectionAsPrimaryAction: Bool](uibarbuttonitem/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var action: Selector?](uibarbuttonitem/action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.
- [var target: AnyObject?](uibarbuttonitem/target.md)
  The object that receives an action when the user selects the item.
### Managing the context menu
- [var menu: UIMenu?](uibarbuttonitem/menu.md)
  The context menu for this button.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uibarbuttonitem/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.
### Customizing item appearance
- [var style: UIBarButtonItem.Style](uibarbuttonitem/style-swift.property.md)
  The style of the item.
- [UIBarButtonItem.Style](uibarbuttonitem/style-swift.enum.md)
  Constants that specify the style of an item.
- [var tintColor: UIColor?](uibarbuttonitem/tintcolor.md)
  The tint color to apply to the button item.
- [var isHidden: Bool](uibarbuttonitem/ishidden.md)
  A Boolean that determines the visibility of the item.
- [var isSelected: Bool](uibarbuttonitem/isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var width: CGFloat](uibarbuttonitem/width.md)
  The width of the item.
- [var possibleTitles: Set<String>?](uibarbuttonitem/possibletitles.md)
  The set of possible titles to display on the bar button.
### Customizing the Back button
- [func backButtonBackgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:).md)
  Returns the back button background image for a specified control state and bar metrics.
- [func setBackButtonBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:).md)
  Sets the back button background image for a specified control state and bar metrics.
- [func backButtonTitlePositionAdjustment(for: UIBarMetrics) -> UIOffset](uibarbuttonitem/backbuttontitlepositionadjustment(for:).md)
  Returns the back button title offset for specified bar metrics.
- [func setBackButtonTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](uibarbuttonitem/setbackbuttontitlepositionadjustment(_:for:).md)
  Sets the back button title offset for specified bar metrics.
- [func backButtonBackgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backbuttonbackgroundverticalpositionadjustment(for:).md)
  Returns the back button vertical position offset for specified bar metrics.
- [func setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(_:for:).md)
  Sets the back button vertical position offset for specified bar metrics.
### Customizing the background
- [func backgroundVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uibarbuttonitem/backgroundverticalpositionadjustment(for:).md)
  Returns the background vertical position offset for specified bar metrics.
- [func setBackgroundVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:).md)
  Sets the background vertical position offset for specified bar metrics.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:barmetrics:).md)
  Returns the background image for a specified state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for a specified state and bar metrics.
- [func backgroundImage(for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?](uibarbuttonitem/backgroundimage(for:style:barmetrics:).md)
  Returns the background image for the specified state, style, and metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics)](uibarbuttonitem/setbackgroundimage(_:for:style:barmetrics:).md)
  Sets the background image for the specified state, style, and metrics.
### Customizing the title placement
- [func titlePositionAdjustment(for: UIBarMetrics) -> UIOffset](uibarbuttonitem/titlepositionadjustment(for:).md)
  Returns the title offset for specified bar metrics.
- [func setTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](uibarbuttonitem/settitlepositionadjustment(_:for:).md)
  Sets the title offset for specified bar metrics.
### Configuring symbol effects
- [var isSymbolAnimationEnabled: Bool](uibarbuttonitem/issymbolanimationenabled.md)
  A Boolean value that indicates whether symbol effects animate.
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-3iew0.md)
  Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-6jx3e.md)
  Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-9dytr.md)
  Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](uibarbuttonitem/setsymbolimage(_:contenttransition:options:).md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-214pl.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-7m567.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-8zc4d.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removeallsymboleffects(options:animated:).md)
  Removes all symbol effects from the bar button item, using the specified options and animation setting.
### Getting the group
- [var buttonGroup: UIBarButtonItemGroup?](uibarbuttonitem/buttongroup.md)
  The group that the button belongs to.
### Representing the item in a menu
- [var menuRepresentation: UIMenuElement?](uibarbuttonitem/menurepresentation.md)
  A menu element that represents the item when it appears in a menu.
### Adding a badge
- [var badge: UIBarButtonItem.Badge?](uibarbuttonitem/badge-4sz3f.md)
- [UIBarButtonItem.Badge](uibarbuttonitem/badge-swift.struct.md)
### Customizing placement in a toolbar
- [var hidesSharedBackground: Bool](uibarbuttonitem/hidessharedbackground.md)
  A boolean value indicating whether the background this item may share with other items in the bar should be hidden.
- [var sharesBackground: Bool](uibarbuttonitem/sharesbackground.md)
  A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.
### Instance Properties
- [var identifier: String?](uibarbuttonitem/identifier.md)
  An identifier used to match bar button items across transitions in a navigation bar or toolbar.

## Relationships

### Inherits From
- [UIBarItem](uibaritem.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIAppearance](uiappearance.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)

## See Also

- [class UIBarItem](uibaritem.md)
  An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem)*