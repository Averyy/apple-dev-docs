# CPListTemplate

**Framework**: Carplay  
**Kind**: class

A template that displays and manages a list of items.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPListTemplate
```

#### Overview

Use the list template to display a list of items, grouped into one or more sections. When the user selects an item, CarPlay invokes Siri or a custom handler that you provide, depending on the type of list item. If your list displays hierarchical data, use the handler to add templates to the navigation hierarchy.

To create a list template, call the [`init(title:sections:)`](cplisttemplate/init(title:sections:).md) method and provide an array of [`CPListSection`](cplistsection.md) objects. At runtime, use [`maximumSectionCount`](cplisttemplate/maximumsectioncount.md) to determine the maximum number of sections your list can display. Use [`maximumItemCount`](cplisttemplate/maximumitemcount.md) to determine the maximum number of items across all sections that your list can display.

Each section contains an array of list items — objects that conform to either the [`CPListTemplateItem`](cplisttemplateitem.md) or the [`CPSelectableListItem`](cpselectablelistitem.md) protocol. CarPlay provides three concrete implementations of these protocols:

> **Note**:  The depth of a hierarchical list in CarPlay depends on your app’s entitlements. Food-ordering apps must not exceed two levels. The framework restricts all other categories of apps to five levels. Also, some vehicles limit the number of items that the list displays. See [`CPSessionConfiguration`](cpsessionconfiguration.md) for more information.

To display the list, call your interface controller’s [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) method, passing in the list template to add it to your navigation hierarchy. Alternatively, add the template as a tab in your [`CPTabBarTemplate`](cptabbartemplate.md).

##### Integrating Siri Into Your Template App

For audio and communication apps, CarPlay provides an  to let users interact with your app using Siri_._

![Screenshot that shows the assistant cell at the top of a list template.](https://docs-assets.developer.apple.com/published/ddb3b9bcc13948f8ba4c7ceeb86fdef5/media-3786976%402x.png)

To enable the assistant cell, your app must support specific Siri intents:

- To play audio, audio apps must support doc://com.apple.documentation/documentation/sirikit/inplaymediaintent.
- To make phone calls, communication apps must support doc://com.apple.documentation/documentation/sirikit/instartcallintent.

To enable the assistant cell in your list template, use [`init(title:sections:assistantCellConfiguration:)`](cplisttemplate/init(title:sections:assistantcellconfiguration:).md) and provide the required configuration. For more information, see [`CPAssistantCellConfiguration`](cpassistantcellconfiguration.md). CarPlay automatically updates your app’s interface if you change the template’s [`assistantCellConfiguration`](cplisttemplate/assistantcellconfiguration.md) property.

## Topics

### Creating a List Template
- [init(title: String?, sections: [CPListSection])](cplisttemplate/init(title:sections:).md)
  Creates a list template with an array of list sections and optional title.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](cplisttemplate/init(title:sections:assistantcellconfiguration:).md)
  Creates a sectioned list template that optionally displays the assistant cell.
### Managing Sections
- [class var maximumSectionCount: Int](cplisttemplate/maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](cplisttemplate/sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](cplisttemplate/updatesections(_:).md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](cplistsection.md)
  A container that groups your list items into sections.
### Managing the Assistant Cell
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](cplisttemplate/assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.
- [class CPAssistantCellConfiguration](cpassistantcellconfiguration.md)
  An object that provides the configuration attributes for the assistant cell.
### Managing an Empty List
- [var emptyViewTitleVariants: [String]](cplisttemplate/emptyviewtitlevariants.md)
  An array of title variants for the template’s empty view.
- [var emptyViewSubtitleVariants: [String]](cplisttemplate/emptyviewsubtitlevariants.md)
  An array of subtitle variants for the template’s empty view.
### Getting Supplementary Information
- [class var maximumItemCount: Int](cplisttemplate/maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [var itemCount: Int](cplisttemplate/itemcount.md)
  The total number of items, across all sections, in the list.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](cplisttemplate/indexpath(for:).md)
  Returns the index path for the specified item.
- [var title: String?](cplisttemplate/title.md)
  The title that the navigation bar displays when the template is visible.
### Responding to List Events
- [var delegate: (any CPListTemplateDelegate)?](cplisttemplate/delegate.md)
  The object that serves as the delegate to the list template.
- [protocol CPListTemplateDelegate](cplisttemplatedelegate.md)
  The interface an object implements to serve as the delegate for a list template.
### Instance Properties
- [var showsSpinnerWhileEmpty: Bool](cplisttemplate/showsspinnerwhileempty.md)
  If YES, a spinning activity indicator will be displayed while the list template contains no items. The activity indicator will be displayed in addition to any @c emptyViewTitleVariants or

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

## See Also

- [class CPGridTemplate](cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPTabBarTemplate](cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPTemplate](cptemplate.md)
  An abstract base class for interface templates.
- [protocol CPBarButtonProviding](cpbarbuttonproviding.md)
  The methods that templates use to provide buttons for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CarPlay/cplisttemplate)*