# delay(_:)

**Framework**: SwiftUI  
**Kind**: method

Delays the start of the animation by the specified number of seconds.

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
func delay(_ delay: TimeInterval) -> Animation
```

#### Return Value

An animation with a delayed start.

#### Discussion

Use this method to delay the start of an animation. For example, the following code animates the height change of two capsules. Animation of the first [`Capsule`](capsule.md) begins immediately. However, animation of the second one doesn’t begin until a half second later.

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                    .animation(.easeInOut, value: adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
                    .animation(.easeInOut.delay(0.5), value: adjustBy)
            }

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

## Parameters

- `delay`: The number of seconds to delay the start of the   animation.

## See Also

- [func repeatCount(Int, autoreverses: Bool) -> Animation](animation/repeatcount(_:autoreverses:).md)
  Repeats the animation for a specific number of times.
- [func repeatForever(autoreverses: Bool) -> Animation](animation/repeatforever(autoreverses:).md)
  Repeats the animation for the lifespan of the view containing the animation.
- [func speed(Double) -> Animation](animation/speed(_:).md)
  Changes the duration of an animation by adjusting its speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/delay(_:))*