# sheet(presentedFrom:)

**Framework**: MapKit  
**Kind**: method

Show map item detail by presenting a sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class func sheet(presentedFrom viewController: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `viewController`: The view controller that will present the sheet.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:))*