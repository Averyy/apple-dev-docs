# CPPointOfInterestTemplate

**Framework**: CarPlay  
**Kind**: class

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

#### Overview

The Point of Interest template displays selectable instances of [`CPPointOfInterest`](cppointofinterest.md) as annotations on the template’s map, and as items in a scrollable picker that the template overlays on the map. When the user selects a point of interest, the template displays a detail card that contains secondary information and optional actions the user can perform. The template manages clustering points of interest, selecting a point of interest, and zooming and panning the map.

To create a Point of Interest template, you call the [`init(title:pointsOfInterest:selectedIndex:)`](cppointofinteresttemplate/init(title:pointsofinterest:selectedindex:).md) method and provide an array of  `CPPointOfInterest` objects to display in the template’s map. Then call your interface controller’s [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) method to push it onto the navigation hierarchy, or add the template as a tab in your [`CPTabBarTemplate`](cptabbartemplate.md).

You must create an object that implements the [`CPPointOfInterestTemplateDelegate`](cppointofinteresttemplatedelegate.md) protocol and set it as the template’s delegate using the [`pointOfInterestDelegate`](cppointofinteresttemplate/pointofinterestdelegate.md) property. The template informs its delegate about changes to the map’s visible region so you can update the points of interest the map displays.

## Topics

### Creating a Point of Interest Template
- [init(title: String, pointsOfInterest: [CPPointOfInterest], selectedIndex: Int)](cppointofinteresttemplate/init(title:pointsofinterest:selectedindex:).md)
  Creates a Point of Interest template with a title, the points of interest to display, and the initial selection’s index.
- [class CPPointOfInterest](cppointofinterest.md)
  An object that describes a point of interest on the template’s map and in its scrollable picker.
### Handling Template Events
- [var pointOfInterestDelegate: (any CPPointOfInterestTemplateDelegate)?](cppointofinteresttemplate/pointofinterestdelegate.md)
  The object that serves as the template’s delegate.
- [protocol CPPointOfInterestTemplateDelegate](cppointofinteresttemplatedelegate.md)
  The methods to handle a Point of Interest template’s events.
### Managing the Picker’s Title
- [var title: String](cppointofinteresttemplate/title.md)
  The scrollable picker’s title.
### Managing the Points of Interest
- [var pointsOfInterest: [CPPointOfInterest]](cppointofinteresttemplate/pointsofinterest.md)
  The points of interest the template displays on the map and in the scrollable picker.
- [func setPointsOfInterest([CPPointOfInterest], selectedIndex: Int)](cppointofinteresttemplate/setpointsofinterest(_:selectedindex:).md)
  Updates the points of interest and the current selection.
- [var selectedIndex: Int](cppointofinteresttemplate/selectedindex.md)
  The current selection’s index.

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

- [class CPInformationTemplate](cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPTextButton](cptextbutton.md)
  A button that displays a stylized title.
- [Integrating CarPlay with your quick-ordering app](integrating-carplay-with-your-quick-ordering-app.md)
  Configure your food-ordering app to work with CarPlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate)*