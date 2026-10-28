# detectionAtOrBeforeTime:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Returns the array of detections in the detection track before a given time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNDetection *) detectionAtOrBeforeTime:(CMTime) time;
```

## Return Value

A number representing a properly time-stamped detection. The return value is only appropriate for discrete detection tracks.

## Parameters

- `time`: The time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-61x7g/detectionatorbeforetime:)*