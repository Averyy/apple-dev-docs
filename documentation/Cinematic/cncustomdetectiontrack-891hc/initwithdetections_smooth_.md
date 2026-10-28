# initWithDetections:smooth:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Initializes a custom detection track with an array of detections, optionally applying smoothing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithDetections:(NSArray<CNDetection *> *) detections smooth:(BOOL) applySmoothing;
```

## Return Value

An object representing a custom detection track with an array of detections, optionally applying smoothing.

## Parameters

- `detections`: An array of detections.
- `applySmoothing`: A flag that instructs the framework to apply a smoothing algorithm. The smoothing algorithm used, is the same that’s used for built-in detections during recording. It compensates for some amount of jitter in the disparity measure by smoothing out variability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cncustomdetectiontrack-891hc/initwithdetections:smooth:)*