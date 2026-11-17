# CPListTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a single-column list of items in one of several visual styles.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPListTemplate
```

```objc
@interface CPListTemplate : CPTemplate
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

A `CPListTemplate` template presents a single column of items in a scrollable interface. Lists are a versatile way to display content, and frequently play a role in interfaces with hierarchical content. For example, an audio app might display playlists or albums using a list template on one page and allow someone to navigate to a second page with a list of individual songs. Similarly, a communication app might display a list of conversations on one page and a list of messages for a selected conversation on another.

To create a list interface, assemble the rows of content you want to display, organize them into sections, and create a `CPListTemplate` object with your data. Display a list template as the root template of your interface or in a tab of a tab bar template. You can also push a list template onto your app’s navigation stack using the [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) method.

For a list template, choosing the right row type is the most important consideration because it determines the appearance of your content. Rows support a variety of formats and visual styles, including grid-like appearances. You can create rows with a single row type or mix and match types to create hybrid experiences. When creating the rows of your template, start with one of the following types:

- **[`CPListItem`](./cplistitem.md)**: A type that displays a single item in the row. Present the row content using strings and an optional image.
- **[`CPListImageRowItem`](./cplistimagerowitem.md)**: A versatile type that supports visually rich layouts and multiple items per row. Row elements present a grid-like appearance.
- **[`CPMessageListItem`](./cpmessagelistitem.md)**: A type that displays message-specific conversation or contact details in a row. This row type is available only to communication apps.
- **[`CPAssistantCellConfiguration`](./cpassistantcellconfiguration.md)**: A type that adds support for app-based interactions using Siri to your list interface. This row type is available only to audio and communication apps.

When configuring the sections and rows of your list template, keep in mind that list interfaces support a finite number of rows and sections. The [`maximumSectionCount`](./cplisttemplate/maximumsectioncount.md) and [`maximumItemCount`](./cplisttemplate/maximumitemcount.md) properties indicate the limits. If you include more items than the maximum values, CarPlay discards items past the specified limits.

In addition to rows, a list interface can display a prominent header with text, images, and interactive buttons above your row content. Specify the header when creating the template, or add it dynamically using the [`listHeader`](./cplisttemplate/listheader.md) property. You can also add header content to each section object to make the start of the section more prominent.

## Topics

### Creating a list template
- [init(title: String?, sections: [CPListSection])](./cplisttemplate/init%28title,sections%29.md)
  Creates a list template with a title and sections to display.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./cplisttemplate/init%28title,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and an assistant cell.
- [init(title: String?, listHeader: CPListTemplateDetailsHeader?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./cplisttemplate/init%28title,listheader,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and a header and assistant cell with optional details.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?, headerGridButtons: [CPGridButton]?)](./cplisttemplate/init%28title,sections,assistantcellconfiguration,headergridbuttons%29.md)
  Creates a list template with a title, sections, an optional assistant cell, and one or more buttons to display in the header.
### Getting the configuration limits
- [class var maximumSectionCount: Int](./cplisttemplate/maximumsectioncount.md)
  The maximum number of sections the template can display.
- [class var maximumItemCount: Int](./cplisttemplate/maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [class var maximumGridButtonImageSize: CGSize](./cplisttemplate/maximumgridbuttonimagesize.md)
  The expected image size for any grid buttons you add to the header.
- [class var maximumHeaderGridButtonCount: Int](./cplisttemplate/maximumheadergridbuttoncount.md)
  The maximum number of grid buttons you can display in the header.
### Managing section content
- [var sectionCount: Int](./cplisttemplate/sectioncount.md)
  The current number of sections in the list.
- [var sections: [CPListSection]](./cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](./cplisttemplate/updatesections%28_%29.md)
  Adds, removes, reorders, or updates the current sections in the list.
### Getting item details
- [var itemCount: Int](./cplisttemplate/itemcount.md)
  The total number of items, across all sections, in the list.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](./cplisttemplate/indexpath%28for%29.md)
  Returns the index path for the specified item.
### Managing the supplemental content
- [var title: String?](./cplisttemplate/title.md)
  The title to display in the navigation bar when the list is visible.
- [var listHeader: CPListTemplateDetailsHeader?](./cplisttemplate/listheader.md)
  An optional header to display between the navigation bar and first section of content.
- [var headerGridButtons: [CPGridButton]?](./cplisttemplate/headergridbuttons.md)
  Buttons to display in the header area above the list content.
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](./cplisttemplate/assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.
### Managing an empty list
- [var showsSpinnerWhileEmpty: Bool](./cplisttemplate/showsspinnerwhileempty.md)
  A Boolean value that indicates whether to display a spinning activity indicator when the list contains no items.
- [var emptyViewTitleVariants: [String]](./cplisttemplate/emptyviewtitlevariants.md)
  An array of localized title strings to display when the list contains no items.
- [var emptyViewSubtitleVariants: [String]](./cplisttemplate/emptyviewsubtitlevariants.md)
  An array of localized subtitle strings to display when the list contains no items.
### Deprecated
- [var delegate: (any CPListTemplateDelegate)?](./cplisttemplate/delegate.md)
  The list template’s delegate is informed of list selection events.
- [protocol CPListTemplateDelegate](./cplisttemplatedelegate.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate)*