# mapItemDetailPopover(item:displaysMap:attachmentAnchor:)

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
@preconcurrency func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool = true, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds)) -> some View
```

#### Discussion

Use this modifier if you want the system to choose the best orientation of the popover’s arrow. If you want to specify a particular edge for the arrow, use `View/mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)`.

## Parameters

- `item`: When   is non- , a detail popover is displayed for the   map item.
- `displaysMap`: If an inline map should be displayed with the place data.   A value of   must be specified if the application UI is not   already showing the place in a map view.
- `attachmentAnchor`: The positioning anchor that defines the attachment   point of the popover. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapitemdetailpopover(item:displaysmap:attachmentanchor:))*