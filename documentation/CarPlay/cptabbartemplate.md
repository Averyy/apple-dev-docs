# CPTabBarTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A container template that displays and manages other templates, presenting them as tabs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPTabBarTemplate
```

```objc
@interface CPTabBarTemplate : CPTemplate
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

`CPTabBarTemplate` is a container template that displays a collection of other templates, where each template occupies a single tab in the tab bar. At runtime, use [`maximumTabCount`](./cptabbartemplate/maximumtabcount.md) to determine the maximum number of tabs that your tab bar can display.

When creating an instance of `CPTabBarTemplate`, provide an array of templates for the tab bar to display. CarPlay treats the array’s templates as root templates, each with its own navigation hierarchy. When a tab bar template is the [`rootTemplate`](./cpinterfacecontroller/roottemplate.md) of your app’s interface controller and you use the controller to add and remove templates, CarPlay applies those changes to the selected tab’s navigation hierarchy.

> **Note**:  You can’t add a tab bar template to an existing navigation hierarchy, or present one modally. Instead, use [`setRootTemplate(_:animated:completion:)`](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md) to set the tab bar as your app’s root template.

Use a transactional approach when making changes to the tab bar. Retrieve the current set of templates using the [`templates`](./cptabbartemplate/templates.md) property. Add, remove, reorder, or make appearance changes to one or more of the array’s templates. For example, use the [`tabTitle`](./cptemplate/tabtitle.md) property to update a template’s tab title, or set [`showsTabBadge`](./cptemplate/showstabbadge.md) to `true` to add an indicator to a template’s tab. Then call the [`updateTemplates(_:)`](./cptabbartemplate/updatetemplates%28_%29.md) method and pass it the updated array. CarPlay commits those changes and updates the tab bar.

When the user selects a tab, the template calls the [`tabBarTemplate(_:didSelect:)`](./cptabbartemplatedelegate/tabbartemplate%28_,didselect%29.md) method on its delegate, which is an object you provide that conforms to the [`CPTabBarTemplateDelegate`](./cptabbartemplatedelegate.md) protocol.

## Topics

### Creating a tab bar template
- [init(templates: [CPTemplate])](./cptabbartemplate/init%28templates%29.md)
  Creates a tab bar template that displays the provided root templates as tabs.
### Responding to tab selections
- [var delegate: (any CPTabBarTemplateDelegate)?](./cptabbartemplate/delegate.md)
  The object that acts as the template’s delegate.
- [protocol CPTabBarTemplateDelegate](./cptabbartemplatedelegate.md)
  The methods an object implements to act as the delegate for a tab bar template.
### Managing the tabs
- [var templates: [CPTemplate]](./cptabbartemplate/templates.md)
  The tab bar’s templates.
- [func updateTemplates([CPTemplate])](./cptabbartemplate/updatetemplates%28_%29.md)
  Adds, removes, reorders, or updates the tab bar’s templates.
- [class var maximumTabCount: Int](./cptabbartemplate/maximumtabcount.md)
  The maximum number of tabs that the template can display.
### Selecting a tab
- [func select(CPTemplate)](./cptabbartemplate/select%28_%29.md)
- [func selectTemplate(at: Int)](./cptabbartemplate/selecttemplate%28at%29.md)
- [var selectedTemplate: CPTemplate?](./cptabbartemplate/selectedtemplate.md)
  The currently selected template in the tab bar.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
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
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate)*