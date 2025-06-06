# nominalFrameRate

**Framework**: AVFoundation  
**Kind**: property

The frame rate of the track, in frames per second.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var nominalFrameRate: Float { get }
```

#### Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/nominalframerate)*