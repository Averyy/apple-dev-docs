# calloutWithCalloutStyle:

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Show map item detail as an annotation callout on the map

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) calloutWithCalloutStyle:(MKMapItemDetailSelectionAccessoryCalloutStyle) style;
```

## Parameters

- `style`: The callout style to use.

## See Also

### Creating a presentation style
- [+ automaticWithPresentationViewController:](./automaticwithpresentationviewcontroller_.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/callout.md)
  Show map item detail as an annotation callout on the map.
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle/sheet%28presentedfrom%29.md)
  Show map item detail by presenting a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/calloutwithcalloutstyle:)*