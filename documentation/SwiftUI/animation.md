# Animation

**Framework**: SwiftUI  
**Kind**: struct

The way a view changes over time to create a smooth visual transition from one state to another.

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
@frozen
struct Animation
```

## Mentions

- [Unifying your app’s animations](unifying-your-app-s-animations.md)

#### Overview

An `Animation` provides a visual transition of a view when a state value changes from one value to another. The characteristics of this transition vary according to the animation type. For instance, a [`linear`](animation/linear.md) animation provides a mechanical feel to the animation because its speed is consistent from start to finish. In contrast, an animation that uses easing, like [`easeOut`](animation/easeout.md), offers a more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the [`animation(_:value:)`](view/animation(_:value:).md) modifier, and specify both an animation type and the value to animate. For instance, the [`Circle`](circle.md) view in the following code performs an [`easeIn`](animation/easein.md) animation each time the state variable `scale` changes:

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
```

When the value of `scale` changes, the modifier [`scaleEffect(_:anchor:)`](view/scaleeffect(_:anchor:).md) resizes [`Circle`](circle.md) according to the new value. SwiftUI can animate the transition between sizes because [`Circle`](circle.md) conforms to the [`Shape`](shape.md) protocol. Shapes in SwiftUI conform to the [`Animatable`](animatable.md) protocol, which describes how to animate a property of a view.

In addition to adding an animation to a view, you can also configure the animation by applying animation modifiers to the animation type. For example, you can:

- Delay the start of the animation by using the [`delay(_:)`](animation/delay(_:).md) modifier.
- Repeat the animation by using the [`repeatCount(_:autoreverses:)`](animation/repeatcount(_:autoreverses:).md) or [`repeatForever(autoreverses:)`](animation/repeatforever(autoreverses:).md) modifiers.
- Change the speed of the animation by using the [`speed(_:)`](animation/speed(_:).md) modifier.

For example, the [`Circle`](circle.md) view in the following code repeats the [`easeIn`](animation/easein.md) animation three times by using the [`repeatCount(_:autoreverses:)`](animation/repeatcount(_:autoreverses:).md) modifier:

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn.repeatCount(3), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
}
```

A view can also perform an animation when a binding value changes. To specify the animation type on a binding, call its [`animation(_:)`](binding/animation(_:).md) method. For example, the view in the following code performs a [`linear`](animation/linear.md) animation, moving the box truck between the leading and trailing edges of the view. The truck moves each time a person clicks the [`Toggle`](toggle.md) control, which changes the value of the `$isTrailing` binding.

```swift
struct ContentView: View {
    @State private var isTrailing = false

    var body: some View {
       VStack(alignment: isTrailing ? .trailing : .leading) {
            Image(systemName: "box.truck")
                .font(.system(size: 64))

            Toggle("Move to trailing edge",
                   isOn: $isTrailing.animation(.linear))
        }
    }
}
```

## Topics

### Getting the default animation
- [static let `default`: Animation](animation/default.md)
  A default animation instance.
### Getting linear animations
- [static var linear: Animation](animation/linear.md)
  An animation that moves at a constant speed.
- [static func linear(duration: TimeInterval) -> Animation](animation/linear(duration:).md)
  An animation that moves at a constant speed during a specified duration.
### Getting eased animations
- [static var easeIn: Animation](animation/easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static func easeIn(duration: TimeInterval) -> Animation](animation/easein(duration:).md)
  An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](animation/easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static func easeOut(duration: TimeInterval) -> Animation](animation/easeout(duration:).md)
  An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [static var easeInOut: Animation](animation/easeinout.md)
  An animation that combines the behaviors of in and out easing animations.
- [static func easeInOut(duration: TimeInterval) -> Animation](animation/easeinout(duration:).md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.
### Getting built-in spring animations
- [static var bouncy: Animation](animation/bouncy.md)
  A spring animation with a predefined duration and higher amount of bounce.
- [static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation](animation/bouncy(duration:extrabounce:).md)
  A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [static var smooth: Animation](animation/smooth.md)
  A smooth spring animation with a predefined duration and no bounce.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation](animation/smooth(duration:extrabounce:).md)
  A smooth spring animation with a predefined duration and no bounce that can be tuned.
- [static var snappy: Animation](animation/snappy.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy.
- [static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation](animation/snappy(duration:extrabounce:).md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.
### Customizing spring animations
- [static var spring: Animation](animation/spring.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static func spring(Spring, blendDuration: TimeInterval) -> Animation](animation/spring(_:blendduration:).md)
  A persistent spring animation.
- [static func spring(duration: TimeInterval, bounce: Double, blendDuration: Double) -> Animation](animation/spring(duration:bounce:blendduration:).md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [static func spring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](animation/spring(response:dampingfraction:blendduration:).md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static var interactiveSpring: Animation](animation/interactivespring.md)
  A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [static func interactiveSpring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](animation/interactivespring(response:dampingfraction:blendduration:).md)
  A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [static var interpolatingSpring: Animation](animation/interpolatingspring.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [static func interpolatingSpring(Spring, initialVelocity: Double) -> Animation](animation/interpolatingspring(_:initialvelocity:).md)
  An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [static func interpolatingSpring(duration: TimeInterval, bounce: Double, initialVelocity: Double) -> Animation](animation/interpolatingspring(duration:bounce:initialvelocity:).md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [static func interpolatingSpring(mass: Double, stiffness: Double, damping: Double, initialVelocity: Double) -> Animation](animation/interpolatingspring(mass:stiffness:damping:initialvelocity:).md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
### Creating custom animations
- [init<A>(A)](animation/init(_:).md)
  Create an `Animation` that contains the specified custom animation.
- [static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation](animation/timingcurve(_:duration:).md)
  Creates a new animation with speed controlled by the given curve.
- [static func timingCurve(Double, Double, Double, Double, duration: TimeInterval) -> Animation](animation/timingcurve(_:_:_:_:duration:).md)
  An animation created from a cubic Bézier timing curve.
### Configuring an animation
- [func delay(TimeInterval) -> Animation](animation/delay(_:).md)
  Delays the start of the animation by the specified number of seconds.
- [func repeatCount(Int, autoreverses: Bool) -> Animation](animation/repeatcount(_:autoreverses:).md)
  Repeats the animation for a specific number of times.
- [func repeatForever(autoreverses: Bool) -> Animation](animation/repeatforever(autoreverses:).md)
  Repeats the animation for the lifespan of the view containing the animation.
- [func speed(Double) -> Animation](animation/speed(_:).md)
  Changes the duration of an animation by adjusting its speed.
### Instance Properties
- [var base: any CustomAnimation](animation/base.md)
### Instance Methods
- [func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V?](animation/animate(value:time:context:).md)
  Calculates the current value of the animation.
- [func logicallyComplete(after: TimeInterval) -> Animation](animation/logicallycomplete(after:).md)
  Causes the animation to report logical completion after the specified duration, if it has not already logically completed.
- [func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval, context: inout AnimationContext<V>) -> Bool](animation/shouldmerge(previous:value:time:context:).md)
  Returns a Boolean value that indicates whether the current animation should merge with a previous animation.
- [func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>) -> V?](animation/velocity(value:time:context:).md)
  Calculates the current velocity of the animation.
### Type Methods
- [static func interactiveSpring(duration: TimeInterval, extraBounce: Double, blendDuration: TimeInterval) -> Animation](animation/interactivespring(duration:extrabounce:blendduration:).md)
  A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](withanimation(_:_:).md)
  Returns the result of recomputing the view’s body with the provided animation.
- [func withAnimation<Result>(Animation?, completionCriteria: AnimationCompletionCriteria, () throws -> Result, completion: () -> Void) rethrows -> Result](withanimation(_:completioncriteria:_:completion:).md)
  Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [struct AnimationCompletionCriteria](animationcompletioncriteria.md)
  The criteria that determines when an animation is considered finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation)*