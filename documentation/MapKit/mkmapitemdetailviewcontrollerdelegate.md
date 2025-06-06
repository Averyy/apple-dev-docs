# MKMapItemDetailViewControllerDelegate

**Framework**: MapKit  
**Kind**: protocol

The methods that you use to receive events from an associated map view controller.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol MKMapItemDetailViewControllerDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func mapItemDetailViewControllerDidFinish(MKMapItemDetailViewController)](mkmapitemdetailviewcontrollerdelegate/mapitemdetailviewcontrollerdidfinish(_:).md)
  Informs the delegate when a person dismissed the view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md)
  An object that displays detailed information about a map item.
- [MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [class MKSelectionAccessory](mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md)
  The style to use for a map item detail callout presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontrollerdelegate)*