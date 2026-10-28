# onDrop(of:isTargeted:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.

**Availability**:
- iOS 13.4+ - Deprecated in 27.2
- iPadOS 13.4+ - Deprecated in 27.2
- Mac Catalyst 13.4+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`onDrop(of:isTargeted:perform:)`](./ondrop%28of,istargeted,perform%29-f15m.md) instead.

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

**Other overloads**:

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider], CGPoint) -> Bool) -> some View
```

```swift
nonisolated
func onDrop(of supportedTypes: [String], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider], CGPoint) -> Bool) -> some View
```

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag and drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.
- `isTargeted`: A binding that updates when a drag and drop operation enters or exits the drop target area. The binding’s value is `true` when the cursor is inside the area, and `false` when the cursor is outside.
- `action`: A closure that takes the dropped content and responds appropriately. The parameter to `action` contains the dropped items, with types specified by `supportedTypes`. Return `true` if the drop operation was successful; otherwise, return `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrop(of:istargeted:perform:)-yro6)*