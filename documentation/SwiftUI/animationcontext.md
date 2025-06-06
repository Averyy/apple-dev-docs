# AnimationContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual values that a custom animation can use to manage state and access a view’s environment.

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
struct AnimationContext<Value> where Value : VectorArithmetic
```

#### Overview

The system provides an `AnimationContext` to a [`CustomAnimation`](customanimation.md) instance so that the animation can store and retrieve values in an instance of [`AnimationState`](animationstate.md). To access these values, use the context’s [`state`](animationcontext/state.md) property.

For more convenient access to state, create an [`AnimationStateKey`](animationstatekey.md) and extend `AnimationContext` to include a computed property that gets and sets the [`AnimationState`](animationstate.md) value. Then use this property instead of [`state`](animationcontext/state.md) to retrieve the state of a custom animation. For example, the following code creates an animation state key named `PausableState`. Then the code extends `AnimationContext` to include the `pausableState` property:

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}

extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

To access the pausable state, the custom animation `PausableAnimation` uses the `pausableState` property instead of the [`state`](animationcontext/state.md) property:

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

The animation can also retrieve environment values of the view that created the animation. To retrieve a view’s environment value, use the context’s [`environment`](animationcontext/environment.md) property. For instance, the following code creates a custom [`EnvironmentValues`](environmentvalues.md) property named `animationPaused`, and the view `PausableAnimationView` uses the property to store the paused state:

```swift
extension EnvironmentValues {
    @Entry var animationPaused: Bool = false
}

struct PausableAnimationView: View {
    @State private var paused = false

    var body: some View {
        VStack {
            ...
        }
        .environment(\.animationPaused, paused)
    }
}
```

Then the custom animation `PausableAnimation` retrieves the paused state from the view’s environment using the [`environment`](animationcontext/environment.md) property:

```swift
struct PausableAnimation: CustomAnimation {
    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused
        ...
    }
}
```

## Topics

### Managing state
- [var state: AnimationState<Value>](animationcontext/state.md)
  The current state of a custom animation.
### Retrieving view environment values
- [var environment: EnvironmentValues](animationcontext/environment.md)
  The current environment of the view that created the custom animation.
### Creating context
- [func withState<T>(AnimationState<T>) -> AnimationContext<T>](animationcontext/withstate(_:).md)
  Creates a new context from another one with a state that you provide.
### Instance Properties
- [var isLogicallyComplete: Bool](animationcontext/islogicallycomplete.md)
  Set this to `true` to indicate that an animation is logically complete.

## See Also

- [protocol CustomAnimation](customanimation.md)
  A type that defines how an animatable value changes over time.
- [struct AnimationState](animationstate.md)
  A container that stores the state for a custom animation.
- [protocol AnimationStateKey](animationstatekey.md)
  A key for accessing animation state values.
- [struct UnitCurve](unitcurve.md)
  A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [struct Spring](spring.md)
  A representation of a spring’s motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcontext)*