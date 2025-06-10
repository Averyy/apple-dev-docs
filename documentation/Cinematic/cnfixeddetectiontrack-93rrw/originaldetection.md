# originalDetection

**Framework**: Cinematic  
**Kind**: property

The original detection based on the fixed detection track.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var originalDetection: CNDetection? { get }
```

#### Discussion

This is the way to determine the time and bounds from which the fixed focus originated. This detection isn’t part of the detection track and has a different detection ID or none.

> ❗ **Important**:  To get a detection from the fixed detection track, use detectionAtOrBeforeTime: instead, which returns a properly time-stamped detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnfixeddetectiontrack-93rrw/originaldetection)*