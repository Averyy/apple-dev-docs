# animationState

**Framework**: RealityKit  
**Kind**: property

The animation state for the action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var animationState: (any AnimationStateProtocol)? { get }
```

#### Discussion

Used to procedurally animate a target value with cross-fading, and additive blending support.

The animation state is available when a bind target along with its type is defined for the action. (See [`AnimationStateProtocol`](animationstateprotocol.md))

The following example returns an animated value to the animation system for the current frame by storing its value within the returned animation state.

```swift
MyCustomAction.subscribe(.updated) { event in
    // The returned state will be nil
    // if the action animation's bind target, and type is not defined.
    guard let animationState = event.animationState else {
       return
    }
    animationState.storeAnimatedValue(myAnimatedResult)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionevent/animationstate)*