# easeInOut

**Framework**: SwiftUI  
**Kind**: property

An animation that combines the behaviors of in and out easing animations.

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
static var easeInOut: Animation { get }
```

#### Return Value

An ease-in ease-out animation with the default duration.

#### Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. An ease in and out animation starts slowly, increasing its speed towards the halfway point, and finally decreasing the speed towards the end of the animation.

The `easeInOut` animation has a default duration of 0.35 seconds. To specify the duration, use the [`easeInOut(duration:)`](animation/easeinout(duration:).md) method.

The following code shows an example of animating the size changes of a [`Circle`](circle.md) using an ease in and out animation.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeInOut, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

## See Also

- [static var easeIn: Animation](animation/easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static func easeIn(duration: TimeInterval) -> Animation](animation/easein(duration:).md)
  An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](animation/easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static func easeOut(duration: TimeInterval) -> Animation](animation/easeout(duration:).md)
  An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [static func easeInOut(duration: TimeInterval) -> Animation](animation/easeinout(duration:).md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/easeinout)*