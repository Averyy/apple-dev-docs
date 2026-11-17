# CPPointOfInterestTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a map with selectable points of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPPointOfInterestTemplate
```

```objc
@interface CPPointOfInterestTemplate : CPTemplate
```

## Overview

The point of interest template displays selectable instances of [`CPPointOfInterest`](./cppointofinterest.md) as annotations on the template’s map, and as items in a scrollable picker that the template overlays on the map. When the user selects a point of interest, the template displays a detail card that contains secondary information and optional actions the user can perform. The template manages clustering points of interest, selecting a point of interest, and zooming and panning the map.

To create a point of interest template, you call the [`init(title:pointsOfInterest:selectedIndex:)`](./cppointofinteresttemplate/init%28title,pointsofinterest,selectedindex%29.md) method and provide an array of  `CPPointOfInterest` objects to display in the template’s map. Then call your interface controller’s [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) method to push it onto the navigation hierarchy, or add the template as a tab in your [`CPTabBarTemplate`](./cptabbartemplate.md).

You must create an object that implements the [`CPPointOfInterestTemplateDelegate`](./cppointofinteresttemplatedelegate.md) protocol and set it as the template’s delegate using the [`pointOfInterestDelegate`](./cppointofinteresttemplate/pointofinterestdelegate.md) property. The template informs its delegate about changes to the map’s visible region so you can update the points of interest the map displays.

## Topics

### Creating a point of interest template
- [init(title: String, pointsOfInterest: [CPPointOfInterest], selectedIndex: Int)](./cppointofinteresttemplate/init%28title,pointsofinterest,selectedindex%29.md)
  Creates a point of interest template with a title, the points of interest to display, and the initial selection’s index.
- [class CPPointOfInterest](./cppointofinterest.md)
  An object that describes a point of interest on the template’s map and in its scrollable picker.
### Handling events
- [var pointOfInterestDelegate: (any CPPointOfInterestTemplateDelegate)?](./cppointofinteresttemplate/pointofinterestdelegate.md)
  The object that serves as the template’s delegate.
- [protocol CPPointOfInterestTemplateDelegate](./cppointofinteresttemplatedelegate.md)
  The methods to handle a point of interest template’s events.
### Managing the picker’s title
- [var title: String](./cppointofinteresttemplate/title.md)
  The scrollable picker’s title.
### Managing the points of interest
- [var pointsOfInterest: [CPPointOfInterest]](./cppointofinteresttemplate/pointsofinterest.md)
  The points of interest the template displays on the map and in the scrollable picker.
- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](./cppointofinteresttemplate/setpointsofinterest%28_,selectedindex%29.md)
  Updates the points of interest and the current selection.
- [var selectedIndex: Int](./cppointofinteresttemplate/selectedindex.md)
  The current selection’s index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate)*