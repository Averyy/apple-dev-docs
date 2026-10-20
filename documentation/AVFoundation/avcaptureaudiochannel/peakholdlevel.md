# peakHoldLevel

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The peak hold power level in decibels.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var peakHoldLevel: Float { get }
```

```objc
@property (nonatomic, readonly) float peakHoldLevel;
```

#### Discussion

This property isn’t key-value observable.

## See Also

### Accessing power levels
- [var averagePowerLevel: Float](./averagepowerlevel.md)
  The instantaneous average power level in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel/peakholdlevel)*