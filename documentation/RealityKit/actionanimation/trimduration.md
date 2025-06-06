# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

The framework calculates `AnimationAction/duration`, but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans `AnimationAction/duration`.

If you set a value for this property and both `AnimationAction/trimStart` and `AnimationAction/trimEnd` are `nil`, the animation observes this property as an edited duration.

A value greater than `AnimationAction/duration` causes the animation to repeat, applying the characteristics defined by `AnimationAction/repeatMode`. Assign this property [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Double/greatestFiniteMagnitude) to repeat indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/trimduration)*