# speed(_:)

**Framework**: SwiftUI  
**Kind**: method

Changes the duration of an animation by adjusting its speed.

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
func speed(_ speed: Double) -> Animation
```

#### Return Value

An animation with the adjusted speed.

#### Discussion

Setting the speed of an animation changes the duration of the animation by a factor of `speed`. A higher speed value causes a faster animation sequence due to a shorter duration. For example, a one-second animation with a speed of `2.0` completes in half the time (half a second).

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    private var oneSecondAnimation: Animation {
       .easeInOut(duration: 1.0)
    }

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
            }
            .animation(oneSecondAnimation.speed(2.0), value: adjustBy)

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

Setting `speed` to a lower number slows the animation, extending its duration. For example, a one-second animation with a speed of `0.25` takes four seconds to complete.

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    private var oneSecondAnimation: Animation {
       .easeInOut(duration: 1.0)
    }

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
            }
            .animation(oneSecondAnimation.speed(0.25), value: adjustBy)

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

## Parameters

- `speed`: The speed at which SwiftUI performs the animation.

## See Also

- [func delay(TimeInterval) -> Animation](animation/delay(_:).md)
  Delays the start of the animation by the specified number of seconds.
- [func repeatCount(Int, autoreverses: Bool) -> Animation](animation/repeatcount(_:autoreverses:).md)
  Repeats the animation for a specific number of times.
- [func repeatForever(autoreverses: Bool) -> Animation](animation/repeatforever(autoreverses:).md)
  Repeats the animation for the lifespan of the view containing the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/speed(_:))*