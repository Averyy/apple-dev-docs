# onTapGesture(count:coordinateSpace:inputKinds:perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func onTapGesture(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all, perform action: @escaping (CGPoint) -> Void) -> some View
```

## Parameters

- `count`: The number of taps or clicks required to trigger the action closure provided in `action`.
- `coordinateSpace`: The coordinate space in which to receive location values.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.
- `action`: The action to perform. This closure receives an input that indicates where the interaction occurred.

## See Also

- [func onTapGesture(count: Int, perform: () -> Void) -> some View](view/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [struct TapGesture](tapgesture.md)
  A gesture that recognizes one or more taps.
- [struct SpatialTapGesture](spatialtapgesture.md)
  A gesture that recognizes one or more taps and reports their location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:inputkinds:perform:))*