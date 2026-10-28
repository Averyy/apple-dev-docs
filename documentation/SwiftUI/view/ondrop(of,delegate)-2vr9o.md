# onDrop(of:delegate:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.

**Availability**:
- iOS 13.4+ - Deprecated in 27.2
- iPadOS 13.4+ - Deprecated in 27.2
- Mac Catalyst 13.4+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`onDrop(of:delegate:)`](./ondrop%28of,delegate%29-6lin8.md) instead.

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], delegate: any DropDelegate) -> some View
```

**Other overloads**:

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], delegate: any DropDelegate) -> some View
```

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag and drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.
- `delegate`: A type that conforms to the `DropDelegate` protocol. You have comprehensive control over drop behavior when you use a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrop(of:delegate:)-2vr9o)*