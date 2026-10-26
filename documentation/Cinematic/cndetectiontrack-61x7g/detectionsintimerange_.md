# detectionsInTimeRange:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Returns the array of detections in the detection track within the given time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (NSArray<CNDetection *> *) detectionsInTimeRange:(CMTimeRange) timeRange;
```

#### Return Value

The array of detections in the detection track within the given time range. The return value is only appropriate for discrete detection tracks.

## Parameters

- `timeRange`: The time range of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-61x7g/detectionsintimerange:)*