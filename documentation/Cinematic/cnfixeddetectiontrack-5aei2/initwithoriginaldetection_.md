# initWithOriginalDetection:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Creates a detection track with fixed focus at the disparity of an existing detection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithOriginalDetection:(CNDetection *) originalDetection;
```

## Return Value

An object representing a detection track with fixed focus at the disparity of an existing detection.

## Discussion

This is the way to determine the time and bounds from which the fixed focus originated. This detection isn’t part of the detection track and has a different detection ID or none.

> ❗ **Important**:  To get a detection from the fixed detection track, use detectionAtOrBeforeTime: instead, which returns a properly time-stamped detection.

## Parameters

- `originalDetection`: The fixed detection track, if it exists, based on the original detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnfixeddetectiontrack-5aei2/initwithoriginaldetection:)*