# currentDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current date of playback.

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
var currentDate: Date? { get }
```

```objc
@property (readonly, nullable) NSDate * currentDate;
```

## Discussion

This value is `nil` if playback doesn’t map to a date.

## See Also

### Inspecting the time and date
- [var currentTime: CMTime](./currenttime.md)
  The current time on the integrated timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currentdate)*