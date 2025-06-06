# onDrop(of:isTargeted:perform:)

**Framework**: RealityKit  
**Kind**: method

Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

#### Discussion

The drop destination is the same size and position as this view.

## Parameters

- `supportedContentTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag-and-drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation   enters or exits the drop target area. The binding’s value is   when   the cursor is inside the area, and   when the cursor is outside.
- `action`: A closure that takes the dropped content and responds   appropriately. The parameter to   contains the dropped   items, with types specified by  . Return    if the drop operation was successful; otherwise, return  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/ondrop(of:istargeted:perform:)-8q7gu)*