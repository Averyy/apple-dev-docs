# onTapGesture(count:coordinateSpace:perform:)

**Framework**: Assignables  
**Kind**: method

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func onTapGesture(count: Int = 1, coordinateSpace: CoordinateSpace = .local, perform action: @escaping (CGPoint) -> Void) -> some View
```

#### Discussion

Use this method to perform the specified `action` when the user clicks or taps on the modified view `count` times. The action closure receives the location of the interaction.

> **Note**: If you create a control that’s functionally equivalent to a `Button`, use `ButtonStyle` to create a customized button instead.

If you create a control that’s functionally equivalent to a `Button`, use `ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of the circle based on the tap location.

```None
struct TapGestureExample: View {
    @State private var location: CGPoint = .zero

    var body: some View {
        Circle()
            .fill(self.location.y > 50 ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .onTapGesture { location in
                self.location = location
            }
    }
}
```

## Parameters

- `count`: The number of taps or clicks required to trigger the action   closure provided in  . Defaults to  .
- `coordinateSpace`: The coordinate space in which to receive   location values. Defaults to  .
- `action`: The action to perform. This closure receives an input   that indicates where the interaction occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/ontapgesture(count:coordinatespace:perform:))*