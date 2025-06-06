# onTapGesture(count:perform:)

**Framework**: Swiftui  
**Kind**: method

Adds an action to perform when this view recognizes a tap gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onTapGesture(count: Int = 1, perform action: @escaping () -> Void) -> some View
```

#### Discussion

Use this method to perform the specified `action` when the user clicks or taps on the view or container `count` times.

> **Note**: If you create a control that’s functionally equivalent to a [`Button`](button.md), use [`ButtonStyle`](buttonstyle.md) to create a customized button instead.

In the example below, the color of the heart images changes to a random color from the `colors` array whenever the user clicks or taps on the view twice:

```swift
struct TapGestureExample: View {
    let colors: [Color] = [.gray, .red, .orange, .yellow,
                           .green, .blue, .purple, .pink]
    @State private var fgColor: Color = .gray

    var body: some View {
        Image(systemName: "heart.fill")
            .resizable()
            .frame(width: 200, height: 200)
            .foregroundColor(fgColor)
            .onTapGesture(count: 2) {
                fgColor = colors.randomElement()!
            }
    }
}
```

![A screenshot of a view of a heart.](https://docs-assets.developer.apple.com/published/83704b234b6271147a2dee7586c1438f/SwiftUI-View-TapGesture%402x.png)

## Parameters

- `count`: The number of taps or clicks required to trigger the action   closure provided in  . Defaults to  .
- `action`: The action to perform.

## See Also

- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [struct TapGesture](tapgesture.md)
  A gesture that recognizes one or more taps.
- [struct SpatialTapGesture](spatialtapgesture.md)
  A gesture that recognizes one or more taps and reports their location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:))*