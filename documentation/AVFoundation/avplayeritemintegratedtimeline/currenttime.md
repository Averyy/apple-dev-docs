# currentTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) CMTime currentTime;
```

## Discussion

During playback of interstitial events that occupy a single point, this value doesn’t change.

## See Also

### Inspecting the time and date
- [var currentDate: Date?](./currentdate.md)
  The current date of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currenttime)*