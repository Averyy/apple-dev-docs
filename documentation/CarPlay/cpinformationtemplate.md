# CPInformationTemplate

**Framework**: CarPlay  
**Kind**: class

A template that provides information for a point of interest, food order, parking location, or charging location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPInformationTemplate
```

#### Overview

An information template displays a list of items, and up to three actions the user can perform.

You use an information template to display informative, actionable content to the user. For example, you might display a summary of the user’s food order, and provide actions to place or cancel the order.

When creating an information template, you populate the list with an array of [`CPInformationItem`](cpinformationitem.md) objects, and provide any contextual actions as an array of [`CPTextButton`](cptextbutton.md) objects. The template then arranges the list’s items using your choice of layout — see [`CPInformationTemplateLayout`](cpinformationtemplatelayout.md) for more information.

To display an information template, call your interface controller’s [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) method to push it onto the navigation hierarchy, or [`presentTemplate(_:animated:completion:)`](cpinterfacecontroller/presenttemplate(_:animated:completion:).md) to present it modally.

> **Note**:  You can’t use `CPInformationTemplate` in apps with the audio entitlement.

## Topics

### Creating an Information Template
- [init(title: String, layout: CPInformationTemplateLayout, items: [CPInformationItem], actions: [CPTextButton])](cpinformationtemplate/init(title:layout:items:actions:).md)
  Creates an information template that displays the provided items using the chosen layout.
### Accessing the Layout
- [var layout: CPInformationTemplateLayout](cpinformationtemplate/layout.md)
  The layout that the template uses to arrange its items.
- [enum CPInformationTemplateLayout](cpinformationtemplatelayout.md)
  The layout that an information template uses to arrange its items.
### Managing the Title
- [var title: String](cpinformationtemplate/title.md)
  The template’s title.
### Managing the Items
- [var items: [CPInformationItem]](cpinformationtemplate/items.md)
  The items that the template displays.
- [class CPInformationItem](cpinformationitem.md)
  A data object that provides content for an information template.
- [class CPInformationRatingItem](cpinformationratingitem.md)
  A data object that provides rated content for an information template.
### Managing the Actions
- [var actions: [CPTextButton]](cpinformationtemplate/actions.md)
  The actions that the template displays.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CPBarButtonProviding](cpbarbuttonproviding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CPPointOfInterestTemplate](cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPTextButton](cptextbutton.md)
  A button that displays a stylized title.
- [Integrating CarPlay with your quick-ordering app](integrating-carplay-with-your-quick-ordering-app.md)
  Configure your food-ordering app to work with CarPlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationtemplate)*