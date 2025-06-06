# MKSelectionAccessory.MapItemDetailPresentationStyle

**Framework**: MapKit  
**Kind**: class

The type of map item detail accessory presentation to use.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class MapItemDetailPresentationStyle
```

## Topics

### Creating a presentation style
- [static func automatic(presentationViewController: UIViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-648ee.md)
  An appropriate presentation style will be chosen automatically.
- [static func automatic(presentationViewController: NSViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-9t9vt.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/callout.md)
  Show map item detail as an annotation callout on the map.
- [static func callout(MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/callout(_:).md)
  Show map item detail as an annotation callout on the map
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:).md)
  Show map item detail by presenting a sheet.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md)
  The methods that you use to receive events from an associated map view controller.
- [class MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md)
  An object that displays detailed information about a map item.
- [class MKSelectionAccessory](mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md)
  The style to use for a map item detail callout presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle)*