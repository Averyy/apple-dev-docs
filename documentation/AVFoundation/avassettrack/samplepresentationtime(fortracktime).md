# samplePresentationTime(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadSamplePresentationTime(forTrackTime:completionHandler:)`](./loadsamplepresentationtime%28fortracktime,completionhandler%29.md) instead.

## Declaration

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

```objc
- (CMTime) samplePresentationTimeForTrackTime:(CMTime) trackTime;
```

#### Return Value

The sample presentation time corresponding to the specified time; otherwise [`invalid`](../../CoreMedia/cmtime/invalid.md) if the time is out of range.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a sample presentation time asynchronously using [`loadSamplePresentationTime(forTrackTime:completionHandler:)`](./loadsamplepresentationtime%28fortracktime,completionhandler%29.md) instead.

## Parameters

- `trackTime`: The track time for which to request the sample presentation time.

## See Also

### Accessing temporal information
- [timeRange](./timerange.md)
  The time range of the track within the overall timeline of the asset.
- [naturalTimeScale](./naturaltimescale.md)
  The natural time scale of the media that a track references.
- [estimatedDataRate](./estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/samplepresentationtime(fortracktime:))*