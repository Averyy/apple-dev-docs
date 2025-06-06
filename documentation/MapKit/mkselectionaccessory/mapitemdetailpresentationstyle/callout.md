# callout(_:)

**Framework**: MapKit  
**Kind**: method

Show map item detail as an annotation callout on the map

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func callout(_ style: MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle = .automatic) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `style`: The callout style to use.

## See Also

- [static func automatic(presentationViewController: UIViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-648ee.md)
  An appropriate presentation style will be chosen automatically.
- [static func automatic(presentationViewController: NSViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-9t9vt.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/callout.md)
  Show map item detail as an annotation callout on the map.
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md)
  Display a small “Open in Apple Maps” link.
- [class func sheet(presentedFrom: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:).md)
  Show map item detail by presenting a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/callout(_:))*