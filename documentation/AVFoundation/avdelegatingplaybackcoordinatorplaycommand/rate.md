# rate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A rate to use when starting playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Float { get }
```

```objc
@property (nonatomic, readonly) float rate;
```

## Discussion

This value is always nonzero.

## See Also

### Accessing command details
- [var itemTime: CMTime](./itemtime.md)
  A time in the item timeline to use to begin playback.
- [var hostClockTime: CMTime](./hostclocktime.md)
  A host clock time to use to begin playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaycommand/rate)*