# linear

**Framework**: SwiftUI  
**Kind**: property

An animation that moves at a constant speed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var linear: Animation { get }
```

#### Return Value

A linear animation with the default duration.

#### Discussion

A linear animation provides a mechanical feel to the motion because its speed is consistent from start to finish of the animation. This constant speed makes a linear animation ideal for animating the movement of objects where changes in the speed might feel awkward, such as with an activity indicator.

The following code shows an example of using linear animation to animate the movement of a circle as it moves between the leading and trailing edges of the view. The circle also animates its color change as it moves across the view.

```swift
struct ContentView: View {
    @State private var isActive = false

    var body: some View {
        VStack(alignment: isActive ? .trailing : .leading) {
            Circle()
                .fill(isActive ? Color.red : Color.blue)
                .frame(width: 50, height: 50)

            Button("Animate") {
                withAnimation(.linear) {
                    isActive.toggle()
                }
            }
            .frame(maxWidth: .infinity)
        }
    }
}
```

The `linear` animation has a default duration of 0.35 seconds. To specify a different duration, use [`linear(duration:)`](animation/linear(duration:).md).

## See Also

- [static func linear(duration: TimeInterval) -> Animation](animation/linear(duration:).md)
  An animation that moves at a constant speed during a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/linear)*