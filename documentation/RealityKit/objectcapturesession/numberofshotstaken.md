# numberOfShotsTaken

**Framework**: RealityKit  
**Kind**: property

The number of shots taken in the entire capture session so far, including both automatic capture and manual capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var numberOfShotsTaken: Int { get }
```

#### Discussion

This number includes shots from all scan passes, flipped or unflipped.  It can be directly compared to the `maximumNumberOfInputImages` to keep track of the memory limits required for reconstruction of this session on-device and whether over-capture mode limits are reached for a given session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/numberofshotstaken)*