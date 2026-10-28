# easeInOut

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

## Return Value

An ease-in ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. An ease in and out animation starts slowly, increasing its speed towards the halfway point, and finally decreasing the speed towards the end of the animation.

The `easeInOut` animation has a default duration of 0.35 seconds. To specify the duration, use the [`easeInOut(duration:)`](./easeinout%28duration%29.md) method.

The following code shows an example of animating the size changes of a [`Circle`](../circle.md) using an ease in and out animation.

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

[Video: A video that shows a circle enlarging, then shrinking to its original size using an ease-in ease-out animation.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/animation-12-easeineaseout.mp4)

## See Also

### Getting eased animations
- [static var easeIn: Animation](./easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static func easeIn(duration: TimeInterval) -> Animation](./easein%28duration%29.md)
  An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](./easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static func easeOut(duration: TimeInterval) -> Animation](./easeout%28duration%29.md)
  An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [static func easeInOut(duration: TimeInterval) -> Animation](./easeinout%28duration%29.md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/easeinout)*