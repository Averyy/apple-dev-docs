# durationOffset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time value by which the system offsets the durations of captions to correct a problem.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var durationOffset: CMTime { get }
```

```objc
@property (readonly) CMTime durationOffset;
```

## Discussion

The value may any numeric value, positive, negative, or zero.

## See Also

### Accessing time offsets
- [var startTimeOffset: CMTime](./starttimeoffset.md)
  The time value by which the system offsets the start times of captions to correct a problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversiontimerangeadjustment/durationoffset)*