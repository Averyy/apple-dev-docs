# mapItemDetailSelectionAccessory(_:)

**Framework**: MapKit  
**Kind**: method

Specifies the selection accessory to display for the selected map item content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapItemDetailSelectionAccessory(_ style: MapItemDetailSelectionAccessoryStyle? = .automatic) -> some MapContent
```

## Parameters

- `style`: The map item detail selection accessory style. If  , no selection accessory appears.

## See Also

- [struct MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle.md)
  The map item detail selection accessory style.
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout(_:).md)
  Presents the accessory as an annotation callout on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:))*