# onTapGesture(count:coordinateSpace:perform:)

**Framework**: FamilyControls  
**Kind**: method

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func onTapGesture(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, perform action: @escaping (CGPoint) -> Void) -> some View
```

#### Discussion

Use this method to perform the specified `action` when the user clicks or taps on the modified view `count` times. The action closure receives the location of the interaction.

> **Note**: If you create a control that’s functionally equivalent to a `Button`, use `ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of the circle based on the tap location.

```swift
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

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/ontapgesture(count:coordinatespace:perform:)-1po6g)*