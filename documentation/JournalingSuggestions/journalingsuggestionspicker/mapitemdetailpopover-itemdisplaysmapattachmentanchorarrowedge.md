# mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)

**Framework**: Journaling Suggestions  
**Kind**: method

Presents a map item detail popover.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool = true, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge) -> some View
```

## Parameters

- `item`: When   is non- , a detail popover is displayed for the   map item.
- `displaysMap`: If an inline map should be displayed with the place data.   A value of   must be specified if the application UI is not   already showing the place in a map view.
- `attachmentAnchor`: The positioning anchor that defines the attachment   point of the popover. The default is  .
- `arrowEdge`: The edge of the   that defines the   location of the popover’s arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapitemdetailpopover(item:displaysmap:attachmentanchor:arrowedge:))*