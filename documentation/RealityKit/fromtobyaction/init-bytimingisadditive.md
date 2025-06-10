# init(by:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new action to animate from the deaultSource by a transform relative to the starting transform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(by: Value, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`defaultSource` → `defaultSource + by`

## Parameters

- `by`: Transform which is used to increment the starting transform. Used to determine the final transform we animate towards.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(by:timing:isadditive:))*