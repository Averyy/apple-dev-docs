# init(from:timing:isAdditive:)

**Framework**: RealityKit  
**Kind**: init

Creates a new from to by action to animate from a specified value, towards the defaultSource value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(from: Value, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false)
```

#### Discussion

`from` → `defaultSource`

## Parameters

- `from`: Value set at the start of the animation.
- `timing`: Controls the progress of the animation.
- `isAdditive`: Specifies whether you can additively blend the output from the action’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:timing:isadditive:))*