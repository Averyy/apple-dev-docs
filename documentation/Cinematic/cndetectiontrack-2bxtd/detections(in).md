# detections(in:)

**Framework**: Cinematic  
**Kind**: method

Returns the array of detections in the detection track within the given time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func detections(in timeRange: CMTimeRange) -> [CNDetection]
```

#### Return Value

The array of detections in the detection track within the given time range. The return value is only appropriate for discrete detection tracks.

## Parameters

- `timeRange`: The time range of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-2bxtd/detections(in:))*