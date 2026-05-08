# AnimationState

**Framework**: SwiftUI  
**Kind**: struct

A container that stores the state for a custom animation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct AnimationState<Value> where Value : VectorArithmetic
```

#### Overview

An [`AnimationContext`](animationcontext.md) uses this type to store state for a [`CustomAnimation`](customanimation.md). To retrieve the stored state of a context, you can use the [`state`](animationcontext/state.md) property. However, a more convenient way to access the animation state is to define an [`AnimationStateKey`](animationstatekey.md) and extend [`AnimationContext`](animationcontext.md) with a computed property that gets and sets the animation state, as shown in the following code:

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    static var defaultValue: Self { .init() }
}

extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

When creating an [`AnimationStateKey`](animationstatekey.md), it’s convenient to define the state values that your custom animation needs. For example, the following code adds the properties `paused` and `pauseTime` to the `PausableState` animation state key:

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

To access the pausable state in a `PausableAnimation`, the follow code calls `pausableState` instead of using the context’s [`state`](animationcontext/state.md) property. And because the animation state key `PausableState` defines properties for state values, the custom animation can read and write those values.

```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

##### Storing State for Secondary Animations

A custom animation can also use `AnimationState` to store the state of a secondary animation. For example, the following code creates an [`AnimationStateKey`](animationstatekey.md) that includes the property `secondaryState`, which a custom animation can use to store other state:

```swift
private struct TargetState<Value: VectorArithmetic>: AnimationStateKey {
    var timeDelta = 0.0
    var valueDelta = Value.zero
    var secondaryState: AnimationState<Value>? = .init()

    static var defaultValue: Self { .init() }
}

extension AnimationContext {
    fileprivate var targetState: TargetState<Value> {
        get { state[TargetState<Value>.self] }
        set { state[TargetState<Value>.self] = newValue }
    }
}
```

The custom animation `TargetAnimation` uses `TargetState` to store state data in `secondaryState` for another animation that runs as part of the target animation.

```swift
struct TargetAnimation: CustomAnimation {
    var base: Animation
    var secondary: Animation

    func animate<V: VectorArithmetic>(value: V, time: Double, context: inout AnimationContext<V>) -> V? {
        var targetValue = value
        if let secondaryState = context.targetState.secondaryState {
            var secondaryContext = context
            secondaryContext.state = secondaryState
            let secondaryValue = value - context.targetState.valueDelta
            let result = secondary.animate(
                value: secondaryValue, time: time - context.targetState.timeDelta,
                context: &secondaryContext)
            if let result = result {
                context.targetState.secondaryState = secondaryContext.state
                targetValue = result + context.targetState.valueDelta
            } else {
                context.targetState.secondaryState = nil
            }
        }
        let result = base.animate(value: targetValue, time: time, context: &context)
        if let result = result {
            targetValue = result
        } else if context.targetState.secondaryState == nil {
            return nil
        }
        return targetValue
}

    func shouldMerge<V: VectorArithmetic>(previous: Animation, value: V, time: Double, context: inout AnimationContext<V>) -> Bool {
        guard let previous = previous.base as? Self else { return false }
        var secondaryContext = context
        if let secondaryState = context.targetState.secondaryState {
            secondaryContext.state = secondaryState
            context.targetState.valueDelta = secondary.animate(
                value: value, time: time - context.targetState.timeDelta,
                context: &secondaryContext) ?? value
        } else {
            context.targetState.valueDelta = value
        }
        // Reset the target each time a merge occurs.
        context.targetState.secondaryState = .init()
        context.targetState.timeDelta = time
        return base.shouldMerge(
            previous: previous.base, value: value, time: time,
            context: &context)
    }
}
```

## Topics

### Creating animation state
- [init()](animationstate/init.md)
  Create an empty state container.
### Accessing custom keys
- [subscript<K>(K.Type) -> K.Value](animationstate/subscript(_:).md)
  Accesses the state for a custom key.

## See Also

- [protocol CustomAnimation](customanimation.md)
  A type that defines how an animatable value changes over time.
- [struct AnimationContext](animationcontext.md)
  Contextual values that a custom animation can use to manage state and access a view’s environment.
- [protocol AnimationStateKey](animationstatekey.md)
  A key for accessing animation state values.
- [struct UnitCurve](unitcurve.md)
  A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [struct Spring](spring.md)
  A representation of a spring’s motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationstate)*