# callout(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Presents the accessory as an annotation callout on the map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func callout(_ style: MapItemDetailSelectionAccessoryStyle.CalloutStyle = .automatic) -> MapItemDetailSelectionAccessoryStyle
```

## Parameters

- `style`: The [`MapItemDetailSelectionAccessoryStyle.CalloutStyle`](./calloutstyle.md) to use.

## See Also

### Place information
- [struct MapItemDetailSelectionAccessoryStyle](../mapitemdetailselectionaccessorystyle.md)
  The map item detail selection accessory style.
- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](../mapcontent/mapitemdetailselectionaccessory%28_%29.md)
  Specifies the selection accessory to display for the selected map item content.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View
](../../SwiftUI/view/mapfeatureselectionaccessory%28_%29.md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View
](../../SwiftUI/view/mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View
](../../SwiftUI/view/mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor,arrowedge%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View
](../../SwiftUI/view/mapitemdetailpopover%28item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View
](../../SwiftUI/view/mapitemdetailpopover%28item,displaysmap,attachmentanchor,arrowedge%29.md)
  Presents a map item detail popover.
- [func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool) -> some View
](../../SwiftUI/view/mapitemdetailsheet%28ispresented,item,displaysmap%29.md)
  Presents a map item detail sheet.
- [func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool) -> some View
](../../SwiftUI/view/mapitemdetailsheet%28item,displaysmap%29.md)
  Presents a map item detail sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapitemdetailselectionaccessorystyle/callout(_:))*