# offset

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the animation begins within the duration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var offset: TimeInterval { get set }
```

#### Discussion

The default value is `0`, which indicates that the animation plays with no offset. Setting a value for this property moves the animation data along the timeline and doesn’t change timing. If you set a `AnimationAction/fillMode` other than [`none`](animationfillmode/none.md), the animation fills the vacant area created by the offset according to the characteristics of the specified fill mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/offset)*