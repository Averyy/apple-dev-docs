# init(to:by:mode:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a action to animate towards a final value. The starting value is determined by adding the inverse of `by` to the specified final value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(to: Value, by: Value, mode: FromToByAction<Value>.TransformMode = .default, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`to - by` → `to`

## Parameters

- `to`: Value set at the end of the animation.
- `by`: Value used to determine the starting value, relative to the end value.
- `mode`: Determines what space the transforms are relative to.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(to:by:mode:timing:isadditive:))*