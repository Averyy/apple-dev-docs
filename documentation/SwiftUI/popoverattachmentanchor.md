# PopoverAttachmentAnchor

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

An attachment anchor for a popover.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum PopoverAttachmentAnchor
```

## Topics

### Getting attachment anchors
- [PopoverAttachmentAnchor.point(_:)](./popoverattachmentanchor/point%28_%29.md)
  The anchor point for the popover expressed as a unit point  that describes possible alignments relative to a SwiftUI view.
- [PopoverAttachmentAnchor.rect(_:)](./popoverattachmentanchor/rect%28_%29.md)
  The anchor point for the popover relative to the source’s frame.

## See Also

### Showing a sheet, cover, or popover
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/sheet%28ispresented,ondismiss,content%29.md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/sheet%28item,ondismiss,content%29.md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/fullscreencover%28ispresented,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/fullscreencover%28item,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](./view/popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](./view/popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/popoverattachmentanchor)*