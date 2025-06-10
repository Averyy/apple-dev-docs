# mapItemDetailSheet(isPresented:item:displaysMap:)

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
@preconcurrency func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool = true) -> some View
```

## Parameters

- `isPresented`: The binding to whether the detail sheet should be shown.
- `item`: The map item to display. If nil, a “loading” view is displayed.
- `displaysMap`: If an inline map should be displayed with the place data.   A value of   must be specified if the application UI is not   already showing the place in a map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapitemdetailsheet(ispresented:item:displaysmap:))*