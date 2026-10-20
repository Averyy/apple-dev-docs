# MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MKMapItemDetailSelectionAccessoryCalloutStyle : NSInteger;
```

#### Overview

In Swift, use [`MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full`](./calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

In Objective-C, use [`MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full`](./calloutstyle/full.md) for map views on iPadOS and macOS. Use a sheet presentation to display full detail place information on iOS.

## Topics

### Enumeration Cases
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.automatic](./calloutstyle/automatic.md)
  A value that allows the framework to choose an appropriate callout style automatically.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.compact](./calloutstyle/compact.md)
  A compact, space-saving callout style.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle.full](./calloutstyle/full.md)
  A rich, detailed callout style that is suitable for large map views.
### Initializers
- [init?(rawValue: Int)](./calloutstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Place information
- [protocol MKMapItemDetailViewControllerDelegate](../../mkmapitemdetailviewcontrollerdelegate.md)
  The methods that you use to receive events from an associated map view controller.
- [class MKMapItemDetailViewController](../../mkmapitemdetailviewcontroller.md)
  An object that displays detailed information about a map item.
- [MKSelectionAccessory.MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [class MKSelectionAccessory](../../mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle)*