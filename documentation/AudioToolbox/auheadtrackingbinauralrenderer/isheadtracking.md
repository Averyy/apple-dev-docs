# isHeadTracking

**Framework**: Audio Toolbox  
**Kind**: property

Indicates whether the host currently has enabled head tracking for this spatial Audio Unit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var isHeadTracking: Bool { get }
```

#### Discussion

The host sets this property when the user enables or disables head tracking. When YES, the spatial Audio Unit should use head tracking data to adjust spatialization. When NO, the host has disabled head tracking.

The Audio Unit should monitor this property to detect changes in head tracking state.

This property supports Key-Value Observing (KVO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auheadtrackingbinauralrenderer/isheadtracking)*