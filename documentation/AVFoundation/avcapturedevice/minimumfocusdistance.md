# minimumFocusDistance

**Framework**: AVFoundation  
**Kind**: property

The capture device’s minimum focus distance in millimeters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var minimumFocusDistance: Int { get }
```

#### Discussion

For virtual cameras, like [`builtInDualCamera`](avcapturedevice/devicetype-swift.struct/builtindualcamera.md) or [`builtInTripleCamera`](avcapturedevice/devicetype-swift.struct/builtintriplecamera.md), this value represents the smallest minimum focus distance of the autofocus-capable cameras that it sources.

This value is `-1` if the distance is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minimumfocusdistance)*