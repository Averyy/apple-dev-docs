# onDrop(of:isTargeted:perform:)

**Framework**: MusicKit  
**Kind**: method

Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider], CGPoint) -> Bool) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag and drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation   enters or exits the drop target area. The binding’s value is    when the cursor is inside the area, and   when the cursor is   outside.
- `action`: A closure that takes the dropped content and responds   appropriately. The first parameter to   contains the dropped   items, with types specified by  . The second   parameter contains the drop location in this view’s coordinate   space. Return   if the drop operation was successful;   otherwise, return  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/ondrop(of:istargeted:perform:)-4f7qe)*