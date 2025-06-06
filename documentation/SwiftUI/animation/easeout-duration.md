# easeOut(duration:)

**Framework**: SwiftUI  
**Kind**: method

An animation with a specified duration that starts quickly and then slows towards the end of the movement.

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
static func easeOut(duration: TimeInterval) -> Animation
```

#### Return Value

An ease-out animation with a specified duration.

#### Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. With an ease out animation, the motion starts quickly and decreases its speed towards the end.

Use `easeOut(duration:)` when you want to specify the time it takes for the animation to complete. Otherwise, use [`easeOut`](animation/easeout.md) to perform the animation for a default length of time.

The following code shows an example of animating the size changes of a [`Circle`](circle.md) using an ease out animation with a duration of one second.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeOut(duration: 1.0), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

## Parameters

- `duration`: The length of time, expressed in seconds, that   the animation takes to complete.

## See Also

- [static var easeIn: Animation](animation/easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static func easeIn(duration: TimeInterval) -> Animation](animation/easein(duration:).md)
  An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](animation/easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static var easeInOut: Animation](animation/easeinout.md)
  An animation that combines the behaviors of in and out easing animations.
- [static func easeInOut(duration: TimeInterval) -> Animation](animation/easeinout(duration:).md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/easeout(duration:))*