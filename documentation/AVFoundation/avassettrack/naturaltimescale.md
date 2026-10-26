# naturalTimeScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The natural time scale of the media that a track references.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`naturalTimeScale`](../avpartialasyncproperty/naturaltimescale.md) asynchronously instead.

## Declaration

```swift
var naturalTimeScale: CMTimeScale { get }
```

```objc
@property (nonatomic, readonly) CMTimeScale naturalTimeScale;
```

## See Also

### Accessing temporal information
- [timeRange](./timerange.md)
  The time range of the track within the overall timeline of the asset.
- [estimatedDataRate](./estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [- samplePresentationTimeForTrackTime:](./samplepresentationtime%28fortracktime%29.md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/naturaltimescale)*