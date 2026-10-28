# dropDestination(for:action:isTargeted:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.2
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use [`dropDestination(for:isEnabled:action:)`](./dropdestination%28for,isenabled,action%29.md) with an `action` that takes a [`DropSession`](../dropsession.md) instead.

## Declaration

```swift
nonisolated
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], CGPoint) -> Bool, isTargeted: @escaping (Bool) -> Void = { _ in }) -> some View where T : Transferable
```

## Return Value

A view that provides a drop destination for a drag operation of the specified type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the same size and position as this view.

```swift
@State private var isDropTargeted = false

var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .dropDestination(for: String.self) { receivedTitles, location in
            animateDrop(at: location)
            process(titles: receivedTitles)
        } isTargeted: {
            isDropTargeted = $0
        }
}

func process(titles: [String]) { ... }
func animateDrop(at: CGPoint) { ... }
```

## Parameters

- `payloadType`: The expected type of the dropped models.
- `action`: A closure that takes the dropped content and responds appropriately. The first parameter to `action` contains the dropped items. The second parameter contains the drop location in this view’s coordinate space. Return `true` if the drop operation was successful; otherwise, return `false`.
- `isTargeted`: A closure that is called when a drag and drop operation enters or exits the drop target area. The received value is `true` when the cursor is inside the area, and `false` when the cursor is outside.

## See Also

### Input and events modifiers
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
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](./focusable%28_,onfocuschange%29.md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](./oncontinuoushover%28coordinatespace,perform%29-8gyrl.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dropdestination(for:action:istargeted:))*