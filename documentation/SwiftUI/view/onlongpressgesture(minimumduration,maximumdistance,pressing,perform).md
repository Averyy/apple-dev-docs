# onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: onLongPressGesture(minimumDuration:maximumDuration:perform:onPressingChanged:))

> **Deprecated**: Use [`onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)`](./onlongpressgesture%28minimumduration,maximumdistance,perform,onpressingchanged%29.md) instead.

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, pressing: ((Bool) -> Void)? = nil, perform action: @escaping () -> Void) -> some View
```

## See Also

### Input and events modifiers
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](./dropdestination%28for,action,istargeted%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](./onchange%28of,perform%29.md)
  Adds an action to perform when the given value changes.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](./ontapgesture%28count,coordinatespace,perform%29-36x9h.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](./onlongpressgesture%28minimumduration,pressing,perform%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](./onpastecommand%28of,perform%29-4f78f.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](./onpastecommand%28of,validator,perform%29-964k1.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](./ondrop%28of,delegate%29-2vr9o.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of:isTargeted:perform:)](./ondrop%28of,istargeted,perform%29.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](./focusable%28_,onfocuschange%29.md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](./oncontinuoushover%28coordinatespace,perform%29-8gyrl.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:))*