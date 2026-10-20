# automatic(presentationViewController:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

An appropriate presentation style will be chosen automatically.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func automatic(presentationViewController: NSViewController? = nil) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `presentationViewController`: Supplying a non-nil presentationViewController will enable sheet presentation, if appropriate.

## See Also

### Creating a presentation style
- [static func automatic(presentationViewController: UIViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./automatic%28presentationviewcontroller%29-648ee.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](./callout.md)
  Show map item detail as an annotation callout on the map.
- [static func callout(MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./callout%28_%29.md)
  Show map item detail as an annotation callout on the map
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](./openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./sheet%28presentedfrom%29.md)
  Show map item detail by presenting a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-9t9vt)*