# onContinuousHover(coordinateSpace:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.2
- macOS 13.0+ - Deprecated in 27.2
- tvOS 16.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`onContinuousHover(coordinateSpace:perform:)`](./oncontinuoushover%28coordinatespace,perform%29-4ehfq.md) instead.

## Declaration

```swift
nonisolated
func onContinuousHover(coordinateSpace: CoordinateSpace = .local, perform action: @escaping (HoverPhase) -> Void) -> some View
```

**Other overloads**:

```swift
nonisolated
func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol = .local, perform action: @escaping (HoverPhase) -> Void) -> some View
```

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the view’s bounds.

## Discussion

Call this method to define a region for detecting pointer movement with the size and position of this view. The following example updates `hoverLocation` and `isHovering` to be based on the phase provided to the closure:

```swift
@State private var hoverLocation: CGPoint = .zero
@State private var isHovering = false

var body: some View {
    VStack {
        Color.red
            .frame(width: 400, height: 400)
            .onContinuousHover { phase in
                switch phase {
                case .active(let location):
                    hoverLocation = location
                    isHovering = true
                case .ended:
                    isHovering = false
                }
            }
            .overlay {
                Rectangle()
                    .frame(width: 50, height: 50)
                    .foregroundColor(isHovering ? .green : .blue)
                    .offset(x: hoverLocation.x, y: hoverLocation.y)
            }
    }
}
```

## Parameters

- `coordinateSpace`: The coordinate space for the location values. Defaults to [`CoordinateSpace.local`](../coordinatespace/local.md).
- `action`: The action to perform whenever the pointer enters, moves within, or exits the view’s bounds. The `action` closure passes the [`HoverPhase.active(_:)`](../hoverphase/active%28_%29.md) phase with the pointer’s coordinates if the pointer is in the view’s bounds; otherwise, it passes [`HoverPhase.ended`](../hoverphase/ended.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-8gyrl)*