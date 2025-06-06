# state

**Framework**: SwiftUI  
**Kind**: property

The current state of a custom animation.

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
var state: AnimationState<Value>
```

#### Discussion

An instance of [`CustomAnimation`](customanimation.md) uses this property to read and write state values as the animation runs.

An alternative to using the `state` property in a custom animation is to create an [`AnimationStateKey`](animationstatekey.md) type and extend [`AnimationContext`](animationcontext.md) with a custom property that returns the state as a custom type. For example, the following code creates a state key named `PausableState`. It’s convenient to store state values in the key type, so the `PausableState` structure includes properties for the stored state values `paused` and `pauseTime`.

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

To provide access the pausable state, the following code extends `AnimationContext` to include the `pausableState` property. This property returns an instance of the custom `PausableState` structure stored in [`state`](animationcontext/state.md), and it can also store a new `PausableState` instance in `state`.

```swift
extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Now a custom animation can use the `pausableState` property instead of the [`state`](animationcontext/state.md) property as a convenient way to read and write state values as the animation runs.

```swift
struct PausableAnimation: CustomAnimation {
    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        ...
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationcontext/state)*