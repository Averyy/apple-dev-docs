# focusable(_:onFocusChange:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.

**Availability**:
- macOS 10.15+ - Deprecated in 12.0
- tvOS 13.0+ - Deprecated in 15.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: Use the [`focusable(_:)`](./focusable%28_%29.md) method instead.

## Declaration

```swift
nonisolated
func focusable(_ isFocusable: Bool = true, onFocusChange: @escaping (Bool) -> Void = { _ in }) -> some View
```

#### Return Value

A view that sets whether a view is focusable, and triggers `onFocusChange` when the view gains or loses focus.

## Parameters

- `isFocusable`: A Boolean value that indicates whether this view is focusable.
- `onFocusChange`: A closure that’s called whenever this view either gains or loses focus. The Boolean parameter to `onFocusChange` is `true` when the view is in focus; otherwise, it’s `false`.

## See Also

### Input and events modifiers
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](./dropdestination%28for,action,istargeted%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](./onchange%28of,perform%29.md)
  Adds an action to perform when the given value changes.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](./ontapgesture%28count,coordinatespace,perform%29-36x9h.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](./onlongpressgesture%28minimumduration,maximumdistance,pressing,perform%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
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
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](./oncontinuoushover%28coordinatespace,perform%29-8gyrl.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusable(_:onfocuschange:))*