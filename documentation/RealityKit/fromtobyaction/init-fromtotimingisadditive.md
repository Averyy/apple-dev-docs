# init(from:to:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new action that interpolates towards a specified final value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(from: Value? = nil, to: Value, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`from` → `to` or `defaultSource` → `to`

## Parameters

- `from`: Value set at the start of the animation, or   to use the default source.
- `to`: Value set at the end of the animation.
- `timing`: Controls the progress of the animation.
- `isAdditive`: A Boolean value that indicates whether the animation system additively blends   the action’s output with the base value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:to:timing:isadditive:))*