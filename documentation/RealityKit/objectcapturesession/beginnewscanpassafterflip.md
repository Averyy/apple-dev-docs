# beginNewScanPassAfterFlip()

**Framework**: RealityKit  
**Kind**: method

Starts the capturing of a new side of the object, to be called after the object is scanned one side and flipped.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func beginNewScanPassAfterFlip()
```

#### Discussion

After capturing one side of an object, the session can be paused and the user can be prompted to flip the object to a new side (e.g. the bottom showing) and then [`beginNewScanPassAfterFlip()`](objectcapturesession/beginnewscanpassafterflip().md) called.   This will transition the session back to the `.ready` state waiting for a new bounding box selection phase to ensure the correct object is captured.   Since the object has been flipped, the miniview capture display in the `ObjectCaptureView`will begin empty after this call.

All captured  images are written to the same output directories and the reconstruction process in [`PhotogrammetrySession`](photogrammetrysession.md) will stitch these multiple captures together automatically.

Note: [`beginNewScanPassAfterFlip()`](objectcapturesession/beginnewscanpassafterflip().md) should be called  the object flipped for best results.

See also [`beginNewScanPass()`](objectcapturesession/beginnewscanpass().md) for the case where the object was not flipped but another capture circle at a different height will be performed on the same side instead.

Calling this function is only valid in object-centric scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/beginnewscanpassafterflip())*