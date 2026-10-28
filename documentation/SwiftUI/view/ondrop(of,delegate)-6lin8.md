# onDrop(of:delegate:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedContentTypes: [UTType], delegate: any DropDelegate) -> some View
```

**Other overloads**:

```swift
nonisolated
func onDrop(of supportedTypes: [String], delegate: any DropDelegate) -> some View
```

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Discussion

To use `Transferable` types directly and access a richer feature set — including support for [`DropSession`](../dropsession.md) — use [`dropDestination(for:isEnabled:action:)`](./dropdestination%28for,isenabled,action%29.md) instead.

## Parameters

- `supportedContentTypes`: The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag and drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.
- `delegate`: A type that conforms to the [`DropDelegate`](../dropdelegate.md) protocol. You have comprehensive control over drop behavior when you use a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrop(of:delegate:)-6lin8)*