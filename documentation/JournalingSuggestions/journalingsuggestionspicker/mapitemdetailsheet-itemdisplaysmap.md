# mapItemDetailSheet(item:displaysMap:)

**Framework**: Journaling Suggestions  
**Kind**: method

Presents a map item detail sheet.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool = true) -> some View
```

## Parameters

- `item`: When   is non- , a detail sheet is displayed for the   map item.
- `displaysMap`: If an inline map should be displayed with the place data.   A value of   must be specified if the application UI is not   already showing the place in a map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapitemdetailsheet(item:displaysmap:))*