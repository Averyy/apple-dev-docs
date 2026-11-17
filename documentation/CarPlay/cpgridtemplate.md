# CPGridTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays and manages a grid of items.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPGridTemplate
```

```objc
@interface CPGridTemplate : CPTemplate
```

## Overview

Use this template to display a grid of items as buttons. When creating the grid template, provide an array of [`CPGridButton`](./cpgridbutton.md) objects. Each button contains a title, an image, and an optional handler that the system invokes after the user taps the button on the CarPlay screen.

When there are more than eight buttons in the array, the template displays only the first eight. When there are more than four buttons, the template balances the display of the buttons betweem two rows.

## Topics

### Creating a grid template
- [init(title: String?, gridButtons: [CPGridButton])](./cpgridtemplate/init%28title,gridbuttons%29.md)
  Creates a grid template with a title and a set of buttons.
- [class var maximumGridButtonImageSize: CGSize](./cpgridtemplate/maximumgridbuttonimagesize.md)
  The expected image size for your @c CPGridButton.
### Getting the grid title
- [var title: String](./cpgridtemplate/title.md)
  The title shown in the grid template’s navigation bar.
- [func updateTitle(String)](./cpgridtemplate/updatetitle%28_%29.md)
### Getting the grid buttons
- [var gridButtons: [CPGridButton]](./cpgridtemplate/gridbuttons.md)
  The array of grid buttons displayed on the template.
- [func updateGridButtons([CPGridButton])](./cpgridtemplate/updategridbuttons%28_%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridtemplate)*