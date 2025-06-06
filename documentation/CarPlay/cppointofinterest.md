# CPPointOfInterest

**Framework**: CarPlay  
**Kind**: class

An object that describes a point of interest on the template’s map and in its scrollable picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPPointOfInterest
```

#### Overview

A point of interest describes a geographical location on a map. It also provides supplementary information about the location, such as a title and summary that the template displays in a scrollable picker and on a detail card. A point of interest also provides the buttons the detail card presents to the user as contextual actions.

You provide an array of `CPPointOfInterest` objects when initializing [`CPPointOfInterestTemplate`](cppointofinteresttemplate.md), or whenever the visible region of the template’s map changes, by calling the template’s [`setPointsOfInterest(_:selectedIndex:)`](cppointofinteresttemplate/setpointsofinterest(_:selectedindex:).md) method.

`CPPointOfInterestTemplate` displays a maximum of twelve points of interest.

## Topics

### Creating a Point of Interest
- [convenience init(location: MKMapItem, title: String, subtitle: String?, summary: String?, detailTitle: String?, detailSubtitle: String?, detailSummary: String?, pinImage: UIImage?)](cppointofinterest/init(location:title:subtitle:summary:detailtitle:detailsubtitle:detailsummary:pinimage:).md)
  Creates a point of interest for a specific location.
### Managing the Map Annotation
- [var location: MKMapItem](cppointofinterest/location.md)
  The map item that contains the point of interest’s geographical information.
- [var pinImage: UIImage?](cppointofinterest/pinimage.md)
  A custom image that the map annotation displays.
### Managing the Picker Item’s Data
- [var title: String](cppointofinterest/title.md)
  The title that the picker’s item displays.
- [var subtitle: String?](cppointofinterest/subtitle.md)
  The subtitle that the picker’s item displays.
- [var summary: String?](cppointofinterest/summary.md)
  The summary that the picker’s item displays.
### Managing the Detail Card’s Data
- [var detailTitle: String?](cppointofinterest/detailtitle.md)
  The detail card’s title.
- [var detailSubtitle: String?](cppointofinterest/detailsubtitle.md)
  The detail card’s subtitle.
- [var detailSummary: String?](cppointofinterest/detailsummary.md)
  The detail card’s summary.
### Managing the Detail Card’s Buttons
- [var primaryButton: CPTextButton?](cppointofinterest/primarybutton.md)
  The detail card’s primary action button.
- [var secondaryButton: CPTextButton?](cppointofinterest/secondarybutton.md)
  The detail card’s secondary action button.
### Attaching Additional Context
- [var userInfo: Any?](cppointofinterest/userinfo.md)
  An opaque value for the point of interest.
### Initializers
- [init(location: MKMapItem, title: String, subtitle: String?, summary: String?, detailTitle: String?, detailSubtitle: String?, detailSummary: String?, pinImage: UIImage?, selectedPinImage: UIImage?)](cppointofinterest/init(location:title:subtitle:summary:detailtitle:detailsubtitle:detailsummary:pinimage:selectedpinimage:).md)
### Instance Properties
- [var selectedPinImage: UIImage?](cppointofinterest/selectedpinimage.md)
### Type Properties
- [class var pinImageSize: CGSize](cppointofinterest/pinimagesize.md)
- [class var selectedPinImageSize: CGSize](cppointofinterest/selectedpinimagesize.md)

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
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(title: String, pointsOfInterest: [CPPointOfInterest], selectedIndex: Int)](cppointofinteresttemplate/init(title:pointsofinterest:selectedindex:).md)
  Creates a Point of Interest template with a title, the points of interest to display, and the initial selection’s index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest)*