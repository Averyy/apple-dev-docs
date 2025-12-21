# duration

**Framework**: RealityKit  
**Kind**: property

The elapsed time for one complete rotation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

The framework sets a value for this property depending on the underlying animation data and the specified `AnimationAction/speed`.

You can override the default duration by defining `AnimationAction/trimStart`, `AnimationAction/trimEnd`, or `AnimationAction/trimDuration`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/duration)*