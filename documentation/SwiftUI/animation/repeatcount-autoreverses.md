# repeatCount(_:autoreverses:)

**Framework**: SwiftUI  
**Kind**: method

Repeats the animation for a specific number of times.

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
func repeatCount(_ repeatCount: Int, autoreverses: Bool = true) -> Animation
```

#### Return Value

An animation that repeats for specific number of times.

#### Discussion

Use this method to repeat the animation a specific number of times. For example, in the following code, the animation moves a truck from one edge of the view to the other edge. It repeats this animation three times.

```swift
struct ContentView: View {
    @State private var driveForward = true

    private var driveAnimation: Animation {
        .easeInOut
        .repeatCount(3, autoreverses: true)
        .speed(0.5)
    }

    var body: some View {
        VStack(alignment: driveForward ? .leading : .trailing, spacing: 40) {
            Image(systemName: "box.truck")
                .font(.system(size: 48))
                .animation(driveAnimation, value: driveForward)

            HStack {
                Spacer()
                Button("Animate") {
                    driveForward.toggle()
                }
                Spacer()
            }
        }
    }
}
```

The first time the animation runs, the truck moves from the leading edge to the trailing edge of the view. The second time the animation runs, the truck moves from the trailing edge to the leading edge because `autoreverse` is `true`. If `autoreverse` were `false`, the truck would jump back to leading edge before moving to the trailing edge. The third time the animation runs, the truck moves from the leading to the trailing edge of the view.

## Parameters

- `repeatCount`: The number of times that the animation repeats. Each   repeated sequence starts at the beginning when   is   .
- `autoreverses`: A Boolean value that indicates whether the animation   sequence plays in reverse after playing forward. Autoreverse counts   towards the  . For instance, a   of one plays   the animation forward once, but it doesn’t play in reverse even if    is  . When   is   and    is  , the animation moves forward, then reverses, then   stops.

## See Also

- [func delay(TimeInterval) -> Animation](animation/delay(_:).md)
  Delays the start of the animation by the specified number of seconds.
- [func repeatForever(autoreverses: Bool) -> Animation](animation/repeatforever(autoreverses:).md)
  Repeats the animation for the lifespan of the view containing the animation.
- [func speed(Double) -> Animation](animation/speed(_:).md)
  Changes the duration of an animation by adjusting its speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/repeatcount(_:autoreverses:))*