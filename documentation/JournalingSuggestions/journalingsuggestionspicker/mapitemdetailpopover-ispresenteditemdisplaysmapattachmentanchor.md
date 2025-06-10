# mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)

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
@preconcurrency func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool = true, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds)) -> some View
```

#### Discussion

Use this modifier if you want the system to choose the best orientation of the popover’s arrow. If you want to specify a particular edge for the arrow, use `View/mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)`.

## Parameters

- `isPresented`: The binding to whether the detail sheet should be shown.
- `item`: The map item to display. If nil, a “loading” view is displayed.
- `displaysMap`: If an inline map should be displayed with the place data.   A value of   must be specified if the application UI is not   already showing the place in a map view.
- `attachmentAnchor`: The positioning anchor that defines the attachment   point of the popover. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:))*