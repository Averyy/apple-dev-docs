# init(from:to:mode:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new action that interpolates towards a specified final transform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(from: Value? = nil, to: Value, mode: FromToByAction<Value>.TransformMode = .default, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`defaultSource` → `to` or `defaultSource` → `to`

## Parameters

- `from`: Transform set at the start of the animation, or   to use the default source.
- `to`: Transform set at the end of the animation.
- `mode`: Determines what space the transforms are relative to.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:to:mode:timing:isadditive:))*