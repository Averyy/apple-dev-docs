# MapItemDetailSelectionAccessoryStyle

**Framework**: MapKit  
**Kind**: struct

The map item detail selection accessory style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
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
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout(_:).md)
  Presents the accessory as an annotation callout on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapitemdetailselectionaccessorystyle)*