# init(from:by:mode:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new action that interpolates from a specified starting transform towards a specified transform, which is relative to the start. Alternatively, interpolates towards the default source if `by` is not supplied.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(from: Value, by: Value? = nil, mode: FromToByAction<Value>.TransformMode = .default, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`from` → `from + by` or `from` → `defaultSource`

## Parameters

- `from`: Transform set at the start of the animation.
- `by`: Transform which is used to increment the starting transform. Used to determine the final transform we animate towards.   Set this to   to animate towards the defaultSource transform.
- `mode`: Determines what space the transforms are relative to.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:by:mode:timing:isadditive:))*