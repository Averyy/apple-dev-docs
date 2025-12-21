# trimEnd

**Framework**: RealityKit  
**Kind**: property

The optional time, in seconds, at which the animation stops.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var trimEnd: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation until `time` = [`duration`](animationgroup/duration.md). If you set a value, the animation edits the duration according to the specified ending time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/trimend)*