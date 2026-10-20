# easeIn(duration:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.

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
static func easeIn(duration: TimeInterval) -> Animation
```

#### Return Value

An ease-in animation with a specified duration.

#### Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. With an ease in animation, the motion starts slowly and increases its speed towards the end.

Use `easeIn(duration:)` when you want to specify the time it takes for the animation to complete. Otherwise, use [`easeIn`](./easein.md) to perform the animation for a default length of time.

The following code shows an example of animating the size changes of a [`Circle`](../circle.md) using an ease in animation with a duration of one second.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeIn(duration: 1.0), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

[Video: A video that shows a circle enlarging for one second, then shrinking for another second to its original size using an ease-in animation.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/animation-09-easein-duration.mp4)

## Parameters

- `duration`: The length of time, expressed in seconds, that the animation takes to complete.

## See Also

### Getting eased animations
- [static var easeIn: Animation](./easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](./easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static func easeOut(duration: TimeInterval) -> Animation](./easeout%28duration%29.md)
  An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [static var easeInOut: Animation](./easeinout.md)
  An animation that combines the behaviors of in and out easing animations.
- [static func easeInOut(duration: TimeInterval) -> Animation](./easeinout%28duration%29.md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/easein(duration:))*