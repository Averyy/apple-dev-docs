# preferredVolume

**Framework**: AVFoundation  
**Kind**: property

The track’s volume preference for playing its audible media.

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
var preferredVolume: Float { get }
```

#### Discussion

The preferred volume for an audio track is typically, but not always, `1.0`. For non-audible tracks, the value is `0.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/preferredvolume)*