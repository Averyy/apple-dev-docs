# mapItemDetailSelectionAccessory(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Specifies the selection accessory to display for the selected map item content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapItemDetailSelectionAccessory(_ style: MapItemDetailSelectionAccessoryStyle? = .automatic) -> some MapContent
```

## Parameters

- `style`: The map item detail selection accessory style. If `nil`, no selection accessory appears.

## See Also

### Place information
- [struct MapItemDetailSelectionAccessoryStyle](../mapitemdetailselectionaccessorystyle.md)
  The map item detail selection accessory style.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View\n](../../SwiftUI/view/mapfeatureselectionaccessory%28_%29.md)
  Specifies the selection accessory to display for a `MapFeature`
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](../mapitemdetailselectionaccessorystyle/callout%28_%29.md)
  Presents the accessory as an annotation callout on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:))*