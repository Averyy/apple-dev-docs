# samplePresentationTime(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

#### Return Value

The sample presentation time corresponding to the specified time; otherwise [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) if the time is out of range.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a sample presentation time asynchronously using [`loadSamplePresentationTime(forTrackTime:completionHandler:)`](avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:).md) instead.

## Parameters

- `trackTime`: The track time for which to request the sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/samplepresentationtime(fortracktime:))*