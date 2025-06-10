# onDrop(of:isTargeted:perform:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

#### Discussion

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag and drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation   enters or exits the drop target area. The binding’s value is    when the cursor is inside the area, and   when the cursor is   outside.
- `action`: A closure that takes the dropped content and responds   appropriately. The parameter to   contains the dropped   items, with types specified by  . Return    if the drop operation was successful; otherwise, return  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/ondrop(of:istargeted:perform:)-3gcdx)*