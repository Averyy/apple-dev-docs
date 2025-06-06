# currentTime

**Framework**: AVFoundation  
**Kind**: property

The current time on the integrated timeline.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var currentTime: CMTime { get }
```

#### Discussion

During playback of interstitial events that occupy a single point, this value doesn’t change.

## See Also

- [var currentDate: Date?](avplayeritemintegratedtimeline/currentdate.md)
  The current date of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currenttime)*