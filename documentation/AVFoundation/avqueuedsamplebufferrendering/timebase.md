# timebase

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The timebase for a renderer.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use an AVSampleBufferVideoRenderer or AVSampleBufferAudioRenderer with a render synchronizer instead

## Declaration

```swift
var timebase: CMTimebase { get }
```

```objc
@property (retain, readonly) CMTimebaseRef timebase;
```

#### Discussion

The timebase governs how time stamps are interpreted by the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/timebase)*