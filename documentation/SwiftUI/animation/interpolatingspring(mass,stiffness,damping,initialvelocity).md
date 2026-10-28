# interpolatingSpring(mass:stiffness:damping:initialVelocity:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.

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
static func interpolatingSpring(mass: Double = 1.0, stiffness: Double, damping: Double, initialVelocity: Double = 0.0) -> Animation
```

## Return Value

A spring animation.

## Parameters

- `mass`: The mass of the object attached to the spring.
- `stiffness`: The stiffness of the spring.
- `damping`: The spring damping value.
- `initialVelocity`: The initial velocity of the spring, as a value in the range [0, 1] representing the magnitude of the value being animated.

## See Also

### Customizing spring animations
- [static var spring: Animation](./spring.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static func spring(Spring, blendDuration: TimeInterval) -> Animation](./spring%28_,blendduration%29.md)
  A persistent spring animation.
- [static func spring(duration: TimeInterval, bounce: Double, blendDuration: Double) -> Animation](./spring%28duration,bounce,blendduration%29.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [static func spring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](./spring%28response,dampingfraction,blendduration%29.md)
  A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [static var interactiveSpring: Animation](./interactivespring.md)
  A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [static func interactiveSpring(response: Double, dampingFraction: Double, blendDuration: TimeInterval) -> Animation](./interactivespring%28response,dampingfraction,blendduration%29.md)
  A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [static var interpolatingSpring: Animation](./interpolatingspring.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [static func interpolatingSpring(Spring, initialVelocity: Double) -> Animation](./interpolatingspring%28_,initialvelocity%29.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [static func interpolatingSpring(duration: TimeInterval, bounce: Double, initialVelocity: Double) -> Animation](./interpolatingspring%28duration,bounce,initialvelocity%29.md)
  An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/interpolatingspring(mass:stiffness:damping:initialvelocity:))*