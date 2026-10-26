# automaticWithPresentationViewController:

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

An appropriate presentation style will be chosen automatically.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) automaticWithPresentationViewController:(UIViewController *) presentationViewController;
```

*macOS*

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) automaticWithPresentationViewController:(NSViewController *) presentationViewController;
```

## Parameters

- `presentationViewController`: Supplying a non-nil presentationViewController will enable sheet presentation, if appropriate.

## See Also

### Creating a presentation style
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/callout.md)
  Show map item detail as an annotation callout on the map.
- [+ calloutWithCalloutStyle:](./calloutwithcalloutstyle_.md)
  Show map item detail as an annotation callout on the map
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/sheet%28presentedfrom%29.md)
  Show map item detail by presenting a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/automaticwithpresentationviewcontroller:)*