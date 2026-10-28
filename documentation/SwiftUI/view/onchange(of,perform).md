# onChange(of:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when the given value changes.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use [`onChange(of:initial:_:)`](./onchange%28of,initial,_%29-8wgw9.md) or [`onChange(of:initial:_:)`](./onchange%28of,initial,_%29-4psgg.md) instead. The trailing closure in each case takes either zero or two input parameters, compared to this method which takes one. Be aware that the replacements have slightly different behavior. This modifier’s closure captures values that represent the state before the change. The new modifiers capture values that correspond to the new state. The new behavior makes it easier to perform updates that rely on values other than the one that caused the modifier’s closure to run.

## Declaration

```swift
nonisolated
func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some View where V : Equatable
```

## Discussion

Use this modifier to trigger a side effect when a value changes, like the value associated with an [`Environment`](../environment.md) value or a [`Binding`](../binding.md). For example, you can clear a cache when you notice that a scene moves to the background:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

```swift
.onChange(of: scenePhase) { newScenePhase in
    if newScenePhase == .background {
        Task.detached(priority: .background) {
            // ...
        }
    }
}
```

The system passes the new value into the closure. If you need the old value, capture it in the closure.

## See Also

### Input and events modifiers
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](./dropdestination%28for,action,istargeted%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:))*