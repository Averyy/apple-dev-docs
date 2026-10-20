# audioTimeStamp

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The time as an audio timestamp.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var audioTimeStamp: AudioTimeStamp { get }
```

```objc
@property (nonatomic, readonly) AudioTimeStamp audioTimeStamp;
```

#### Discussion

This is useful for compatibility with lower-level Core Audio and Audio Toolbox API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/audiotimestamp)*