# Animation

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

- [Unifying your app’s animations](./unifying-your-app-s-animations.md)

## Overview

An `Animation` provides a visual transition of a view when a state value changes from one value to another. The characteristics of this transition vary according to the animation type. For instance, a [`linear`](./animation/linear.md) animation provides a mechanical feel to the animation because its speed is consistent from start to finish. In contrast, an animation that uses easing, like [`easeOut`](./animation/easeout.md), offers a more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the [`animation(_:value:)`](./view/animation%28_,value%29.md) modifier, and specify both an animation type and the value to animate. For instance, the [`Circle`](./circle.md) view in the following code performs an [`easeIn`](./animation/easein.md) animation each time the state variable `scale` changes:

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

[Video: A video that shows a circle enlarging then shrinking to its original size using an ease-in animation.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/animation-01-overview-easein.mp4)

When the value of `scale` changes, the modifier [`scaleEffect(_:anchor:)`](./view/scaleeffect%28_,anchor%29.md) resizes [`Circle`](./circle.md) according to the new value. SwiftUI can animate the transition between sizes because [`Circle`](./circle.md) conforms to the [`Shape`](./shape.md) protocol. Shapes in SwiftUI conform to the [`Animatable`](./animatable.md) protocol, which describes how to animate a property of a view.

In addition to adding an animation to a view, you can also configure the animation by applying animation modifiers to the animation type. For example, you can:

- Delay the start of the animation by using the [`delay(_:)`](./animation/delay%28_%29.md) modifier.
- Repeat the animation by using the [`repeatCount(_:autoreverses:)`](./animation/repeatcount%28_,autoreverses%29.md) or [`repeatForever(autoreverses:)`](./animation/repeatforever%28autoreverses%29.md) modifiers.
- Change the speed of the animation by using the [`speed(_:)`](./animation/speed%28_%29.md) modifier.

For example, the [`Circle`](./circle.md) view in the following code repeats the [`easeIn`](./animation/easein.md) animation three times by using the [`repeatCount(_:autoreverses:)`](./animation/repeatcount%28_,autoreverses%29.md) modifier:

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

[Video: A video that shows a circle that repeats the ease-in animation three times: enlarging, then shrinking, then enlarging again. The animation reverses causing the circle to shrink, then enlarge, then shrink to its original size.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/animation-02-overview-easein-repeat.mp4)

A view can also perform an animation when a binding value changes. To specify the animation type on a binding, call its [`animation(_:)`](./binding/animation%28_%29.md) method. For example, the view in the following code performs a [`linear`](./animation/linear.md) animation, moving the box truck between the leading and trailing edges of the view. The truck moves each time a person clicks the [`Toggle`](./toggle.md) control, which changes the value of the `$isTrailing` binding.

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

[Video: A video that shows a box truck that moves from the leading edge of a view to the trailing edge. The box truck then returns to the view's leading edge.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/animation-03-overview-binding.mp4)

## Topics

### Getting the default animation
- [static let `default`: Animation](./animation/default.md)
  A default animation instance.
### Getting linear animations
- [static var linear: Animation](./animation/linear.md)
  An animation that moves at a constant speed.
- [static func linear(duration: TimeInterval) -> Animation](./animation/linear%28duration%29.md)
  An animation that moves at a constant speed during a specified duration.
### Getting eased animations
- [static var easeIn: Animation](./animation/easein.md)
  An animation that starts slowly and then increases speed towards the end of the movement.
- [static func easeIn(duration: TimeInterval) -> Animation](./animation/easein%28duration%29.md)
  An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [static var easeOut: Animation](./animation/easeout.md)
  An animation that starts quickly and then slows towards the end of the movement.
- [static func easeOut(duration: TimeInterval) -> Animation](./animation/easeout%28duration%29.md)
  An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [static var easeInOut: Animation](./animation/easeinout.md)
  An animation that combines the behaviors of in and out easing animations.
- [static func easeInOut(duration: TimeInterval) -> Animation](./animation/easeinout%28duration%29.md)
  An animation with a specified duration that combines the behaviors of in and out easing animations.
### Getting built-in spring animations
- [static var bouncy: Animation](./animation/bouncy.md)
  A spring animation with a predefined duration and higher amount of bounce.
- [static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation](./animation/bouncy%28duration,extrabounce%29.md)
  A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [static var smooth: Animation](./animation/smooth.md)
  A smooth spring animation with a predefined duration and no bounce.
- [static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation](./animation/smooth%28duration,extrabounce%29.md)
  A smooth spring animation with a predefined duration and no bounce that can be tuned.
- [static var snappy: Animation](./animation/snappy.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy.
- [static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation](./animation/snappy%28duration,extrabounce%29.md)
  A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.
### Customizing spring animations
- [static var spring: Animation](./animation/spring.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static func spring(Spring, blendDuration: TimeInterval) -> Animation](./animation/spring%28_,blendduration%29.md)
  A persistent spring animation.
- [static func spring(duration: TimeInterval, bounce: Double, blendDuration: Double) -> Animation](./animation/spring%28duration,bounce,blendduration%29.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [static func spring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](./animation/spring%28response,dampingfraction,blendduration%29.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static var interactiveSpring: Animation](./animation/interactivespring.md)
  A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [static func interactiveSpring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](./animation/interactivespring%28response,dampingfraction,blendduration%29.md)
  A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [static var interpolatingSpring: Animation](./animation/interpolatingspring.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [static func interpolatingSpring(Spring, initialVelocity: Double) -> Animation](./animation/interpolatingspring%28_,initialvelocity%29.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [static func interpolatingSpring(duration: TimeInterval, bounce: Double, initialVelocity: Double) -> Animation](./animation/interpolatingspring%28duration,bounce,initialvelocity%29.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [static func interpolatingSpring(mass: Double, stiffness: Double, damping: Double, initialVelocity: Double) -> Animation](./animation/interpolatingspring%28mass,stiffness,damping,initialvelocity%29.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
### Creating custom animations
- [init<A>(A)](./animation/init%28_%29.md)
  Create an `Animation` that contains the specified custom animation.
- [static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation](./animation/timingcurve%28_,duration%29.md)
  Creates a new animation with speed controlled by the given curve.
- [static func timingCurve(Double, Double, Double, Double, duration: TimeInterval) -> Animation](./animation/timingcurve%28_,_,_,_,duration%29.md)
  An animation created from a cubic Bézier timing curve.
### Configuring an animation
- [func delay(TimeInterval) -> Animation](./animation/delay%28_%29.md)
  Delays the start of the animation by the specified number of seconds.
- [func repeatCount(Int, autoreverses: Bool) -> Animation](./animation/repeatcount%28_,autoreverses%29.md)
  Repeats the animation for a specific number of times.
- [func repeatForever(autoreverses: Bool) -> Animation](./animation/repeatforever%28autoreverses%29.md)
  Repeats the animation for the lifespan of the view containing the animation.
- [func speed(Double) -> Animation](./animation/speed%28_%29.md)
  Changes the duration of an animation by adjusting its speed.
### Instance Properties
- [var base: any CustomAnimation](./animation/base.md)
### Instance Methods
- [func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V?](./animation/animate%28value,time,context%29.md)
  Calculates the current value of the animation.
- [func logicallyComplete(after: TimeInterval) -> Animation](./animation/logicallycomplete%28after%29.md)
  Causes the animation to report logical completion after the specified duration, if it has not already logically completed.
- [func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval, context: inout AnimationContext<V>) -> Bool](./animation/shouldmerge%28previous,value,time,context%29.md)
  Returns a Boolean value that indicates whether the current animation should merge with a previous animation.
- [func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>) -> V?](./animation/velocity%28value,time,context%29.md)
  Calculates the current velocity of the animation.
### Type Properties
- [static var systemOverlayAppearance: Animation](./animation/systemoverlayappearance.md)
  Animation used when system overlays appear.
- [static var systemOverlayDelayedDisappearance: Animation](./animation/systemoverlaydelayeddisappearance.md)
  Animation used when system overlays disappear, with a delay equal to `systemOverlayDisappearanceDelay`.
- [static var systemOverlayDisappearance: Animation](./animation/systemoverlaydisappearance.md)
  Animation used when system overlays disappear.
- [static var systemOverlayDisappearanceDelay: TimeInterval](./animation/systemoverlaydisappearancedelay.md)
  The length of time system overlays remain visible before disappearing.
### Type Methods
- [static func interactiveSpring(duration: TimeInterval, extraBounce: Double, blendDuration: TimeInterval) -> Animation](./animation/interactivespring%28duration,extrabounce,blendduration%29.md)
  A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding state-based animation to an action
- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](./withanimation%28_,_%29.md)
  Returns the result of recomputing the view’s body with the provided animation.
- [func withAnimation<Result>(Animation?, completionCriteria: AnimationCompletionCriteria, () throws -> Result, completion: () -> Void) rethrows -> Result](./withanimation%28_,completioncriteria,_,completion%29.md)
  Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [struct AnimationCompletionCriteria](./animationcompletioncriteria.md)
  The criteria that determines when an animation is considered finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation)*