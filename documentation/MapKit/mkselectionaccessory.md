# MKSelectionAccessory

**Framework**: MapKit  
**Kind**: class

The type of accessory to display for a selected annotation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class MKSelectionAccessory
```

## Mentions

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)

#### Overview

Implement [`mapView(_:selectionAccessoryFor:)`](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md) in your map view delegate to specify a selection accessory for annotation content.

## Topics

### Creating a selection accessory
- [class func mapItemDetail(MKSelectionAccessory.MapItemDetailPresentationStyle) -> MKSelectionAccessory](mkselectionaccessory/mapitemdetail(_:).md)
  Detailed information about a place

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
- [MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md)
  The style to use for a map item detail callout presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory)*