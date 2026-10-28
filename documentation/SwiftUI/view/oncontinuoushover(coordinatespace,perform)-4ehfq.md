# onContinuousHover(coordinateSpace:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol = .local, perform action: @escaping (HoverPhase) -> Void) -> some View
```

**Other overloads**:

```swift
nonisolated
func onContinuousHover(coordinateSpace: CoordinateSpace = .local, perform action: @escaping (HoverPhase) -> Void) -> some View
```

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a view. The following example updates a small rectangle’s position and style by modifying `hoverLocation` and `isHovering` as the pointer moves within the larger, red rectangle:

```swift
@State private var hoverLocation: CGPoint = .zero
@State private var isHovering = false

var body: some View {
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
                .foregroundStyle(isHovering ? .green : .blue)
                .offset(x: hoverLocation.x, y: hoverLocation.y)
        }
}
```

## Parameters

- `coordinateSpace`: The coordinate space for the location values. The default value is [`CoordinateSpace.local`](../coordinatespace/local.md).
- `action`: The action to perform whenever the pointer enters, moves within, or exits the view’s bounds. The closure takes a `phase` input that has the value [`HoverPhase.active(_:)`](../hoverphase/active%28_%29.md) and contains the pointer’s coordinates if the pointer is within the view’s bounds. The closure receives the [`HoverPhase.ended`](../hoverphase/ended.md) phase when the pointer leaves the view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-4ehfq)*