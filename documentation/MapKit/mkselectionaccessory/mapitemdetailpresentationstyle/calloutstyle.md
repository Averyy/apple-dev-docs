# MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle

**Framework**: MapKit  
**Kind**: enum

The style to use for a map item detail callout presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum CalloutStyle
```

#### Overview

In Swift, use [`MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full`](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

In Objective-C, use [`MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full`](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

## Topics

### Enumeration Cases
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.automatic](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/automatic.md)
  A value that allows the framework to choose an appropriate callout style automatically.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.compact](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/compact.md)
  A compact, space-saving callout style.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/full.md)
  A rich, detailed callout style that is suitable for large map views.
### Initializers
- [init?(rawValue: Int)](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md)
  The methods that you use to receive events from an associated map view controller.
- [class MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md)
  An object that displays detailed information about a map item.
- [MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [class MKSelectionAccessory](mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle)*