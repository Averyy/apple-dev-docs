# onContinuousHover(coordinateSpace:perform:)

**Framework**: Assignables  
**Kind**: method

Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onContinuousHover(coordinateSpace: CoordinateSpace = .local, perform action: @escaping (HoverPhase) -> Void) -> some View
```

#### Return Value

A view that calls `action` when the pointer enters, moves within, or exits the view’s bounds.

#### Discussion

Call this method to define a region for detecting pointer movement with the size and position of this view. The following example updates `hoverLocation` and `isHovering` to be based on the phase provided to the closure:

```None
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

- `coordinateSpace`: The coordinate space for the   location values. Defaults to  .
- `action`: The action to perform whenever the pointer enters,   moves within, or exits the view’s bounds. The   closure   passes the   phase with the pointer’s   coordinates if the pointer is in the view’s bounds; otherwise, it   passes  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/oncontinuoushover(coordinatespace:perform:))*