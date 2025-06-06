# sessionID

**Framework**: RealityKit  
**Kind**: property

If captured with `ObjectCaptureSession`, this will contain a UUID associated with the session. Note that any `boundingBox` or camera pose information will only be in a consistent coordinate system if the `sessionID` for those samples is the same.  In this sense, the `sessionID` is a tag that defines the coordinate system of all poses and transforms when comparing samples from multiple captures.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var sessionID: UUID? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/sessionid)*