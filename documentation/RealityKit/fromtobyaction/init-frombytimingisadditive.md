# init(from:by:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new action that interpolates towards a specified value, which is relative to the starting value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(from: Value? = nil, by: Value, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`from` → `from + by` or `defaultSource` → `defaultSource + by`

## Parameters

- `from`: Value set at the start of the animation, or   to use the default source.
- `by`: Value relative to the initial value to determine the final value.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:by:timing:isadditive:))*