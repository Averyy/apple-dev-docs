# onDrop(of:delegate:)

**Framework**: FamilyControls  
**Kind**: method

Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], delegate: any DropDelegate) -> some View
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the   types of content this view can accept through drag and drop.   If the drag and drop operation doesn’t contain any of the supported   types, then this drop destination doesn’t activate and    doesn’t update.
- `delegate`: A type that conforms to the   protocol. You   have comprehensive control over drop behavior when you use a   delegate.

## See Also

- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-647xj.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-6kw8i.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondrop(of:delegate:)-3cx1m)*