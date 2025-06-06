# userCompletedScanPass

**Framework**: RealityKit  
**Kind**: property

This property starts out `false` at the start of a capture and will switch to `true` when the user has moved the device in a full circular scan pass around the bounding box of the target object and captured enough data to fill completely the capture dial.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var userCompletedScanPass: Bool { get }
```

#### Discussion

It is reset to `false` in a given capture session whenever either:

1. [`beginNewScanPassAfterFlip()`](objectcapturesession/beginnewscanpassafterflip().md) is called to start a new scan pass for a flipped object. or
2. [`beginNewScanPass()`](objectcapturesession/beginnewscanpass().md) is called to start a new scan pass on an unflipped object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/usercompletedscanpass)*