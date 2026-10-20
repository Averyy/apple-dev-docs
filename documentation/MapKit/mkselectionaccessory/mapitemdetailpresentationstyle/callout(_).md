# callout(_:)

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

```swift
static func callout(_ style: MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle = .automatic) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `style`: The callout style to use.

## See Also

### Creating a presentation style
- [static func automatic(presentationViewController: UIViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./automatic%28presentationviewcontroller%29-648ee.md)
  An appropriate presentation style will be chosen automatically.
- [static func automatic(presentationViewController: NSViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./automatic%28presentationviewcontroller%29-9t9vt.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](./callout.md)
  Show map item detail as an annotation callout on the map.
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](./openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./sheet%28presentedfrom%29.md)
  Show map item detail by presenting a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/callout(_:))*