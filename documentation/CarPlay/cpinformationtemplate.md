# CPInformationTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

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

```objc
@interface CPInformationTemplate : CPTemplate
```

## Overview

An information template displays a list of items, and up to three actions the user can perform.

You use an information template to display informative, actionable content to the user. For example, you might display a summary of the user’s food order, and provide actions to place or cancel the order.

When creating an information template, you populate the list with an array of [`CPInformationItem`](./cpinformationitem.md) objects, and provide any contextual actions as an array of [`CPTextButton`](./cptextbutton.md) objects. The template then arranges the list’s items using your choice of layout — see [`CPInformationTemplateLayout`](./cpinformationtemplatelayout.md) for more information.

To display an information template, call your interface controller’s [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) method to push it onto the navigation hierarchy, or [`presentTemplate(_:animated:completion:)`](./cpinterfacecontroller/presenttemplate%28_,animated,completion%29.md) to present it modally.

> **Note**:  You can’t use `CPInformationTemplate` in apps with the audio entitlement.

## Topics

### Creating an information template
- [init(title: String, layout: CPInformationTemplateLayout, items: [CPInformationItem], actions: [CPTextButton])](./cpinformationtemplate/init%28title,layout,items,actions%29.md)
  Creates an information template that displays the provided items using the chosen layout.
### Accessing the layout
- [var layout: CPInformationTemplateLayout](./cpinformationtemplate/layout.md)
  The layout that the template uses to arrange its items.
- [enum CPInformationTemplateLayout](./cpinformationtemplatelayout.md)
  The layout that an information template uses to arrange its items.
### Managing the title
- [var title: String](./cpinformationtemplate/title.md)
  The template’s title.
### Managing the items
- [var items: [CPInformationItem]](./cpinformationtemplate/items.md)
  The items that the template displays.
- [class CPInformationItem](./cpinformationitem.md)
  A data object that provides content for an information template.
- [class CPInformationRatingItem](./cpinformationratingitem.md)
  A data object that provides rated content for an information template.
### Managing the actions
- [var actions: [CPTextButton]](./cpinformationtemplate/actions.md)
  The actions that the template displays.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CPBarButtonProviding](./cpbarbuttonproviding.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface templates
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationtemplate)*