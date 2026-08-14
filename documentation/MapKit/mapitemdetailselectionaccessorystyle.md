# MapItemDetailSelectionAccessoryStyle

**Framework**: MapKit  
**Kind**: struct

The map item detail selection accessory style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct MapItemDetailSelectionAccessoryStyle
```

## Topics

### Accessory styles
- [static var automatic: MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/automatic.md)
  A value that allows the framework to choose an appropriate callout style automatically.
- [static var callout: MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout.md)
  The accessory, shown as an annotation callout on the map.
- [static var caption: MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/caption.md)
  An “Open in Apple Maps” link below the content’s label.
- [static var sheet: MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/sheet.md)
  The map item detail sheet.
### Callout styles
- [MapItemDetailSelectionAccessoryStyle.CalloutStyle](mapitemdetailselectionaccessorystyle/calloutstyle.md)
  The style to use for callout content.
- [static var automatic: MapItemDetailSelectionAccessoryStyle.CalloutStyle](mapitemdetailselectionaccessorystyle/calloutstyle/automatic.md)
  A value that allows the framework to choose an appropriate callout style automatically.
- [static var compact: MapItemDetailSelectionAccessoryStyle.CalloutStyle](mapitemdetailselectionaccessorystyle/calloutstyle/compact.md)
  A compact, space-saving callout style.
- [static var full: MapItemDetailSelectionAccessoryStyle.CalloutStyle](mapitemdetailselectionaccessorystyle/calloutstyle/full.md)
  A rich, detailed callout style that is suitable for large map views.
### Type Methods
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout(_:).md)
  Presents the accessory as an annotation callout on the map.

## See Also

- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](mapcontent/mapitemdetailselectionaccessory(_:).md)
  Specifies the selection accessory to display for the selected map item content.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View
](../swiftui/view/mapfeatureselectionaccessory(_:).md)
  Specifies the selection accessory to display for a `MapFeature`
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout(_:).md)
  Presents the accessory as an annotation callout on the map.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View
](../swiftui/view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View
](../swiftui/view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View
](../swiftui/view/mapitemdetailpopover(item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View
](../swiftui/view/mapitemdetailpopover(item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool) -> some View
](../swiftui/view/mapitemdetailsheet(ispresented:item:displaysmap:).md)
  Presents a map item detail sheet.
- [func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool) -> some View
](../swiftui/view/mapitemdetailsheet(item:displaysmap:).md)
  Presents a map item detail sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapitemdetailselectionaccessorystyle)*