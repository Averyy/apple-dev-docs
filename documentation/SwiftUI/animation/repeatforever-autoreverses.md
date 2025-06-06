# repeatForever(autoreverses:)

**Framework**: SwiftUI  
**Kind**: method

Repeats the animation for the lifespan of the view containing the animation.

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
func repeatForever(autoreverses: Bool = true) -> Animation
```

#### Return Value

An animation that continuously repeats.

#### Discussion

Use this method to repeat the animation until the instance of the view no longer exists, or the view’s explicit or structural identity changes. For example, the following code continuously rotates a gear symbol for the lifespan of the view.

```swift
struct ContentView: View {
    @State private var rotationDegrees = 0.0

    private var animation: Animation {
        .linear
        .speed(0.1)
        .repeatForever(autoreverses: false)
    }

    var body: some View {
        Image(systemName: "gear")
            .font(.system(size: 86))
            .rotationEffect(.degrees(rotationDegrees))
            .onAppear {
                withAnimation(animation) {
                    rotationDegrees = 360.0
                }
            }
    }
}
```

## Parameters

- `autoreverses`: A Boolean value that indicates whether the   animation sequence plays in reverse after playing forward.

## See Also

- [func delay(TimeInterval) -> Animation](animation/delay(_:).md)
  Delays the start of the animation by the specified number of seconds.
- [func repeatCount(Int, autoreverses: Bool) -> Animation](animation/repeatcount(_:autoreverses:).md)
  Repeats the animation for a specific number of times.
- [func speed(Double) -> Animation](animation/speed(_:).md)
  Changes the duration of an animation by adjusting its speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/repeatforever(autoreverses:))*