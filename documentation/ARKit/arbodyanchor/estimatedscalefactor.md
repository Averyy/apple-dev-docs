# estimatedScaleFactor

**Framework**: ARKit  
**Kind**: property

A factor that relates the body’s default height with the height ARKit estimates at runtime.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var estimatedScaleFactor: CGFloat { get }
```

#### Discussion

The default value is 1.0. If you set [`automaticSkeletonScaleEstimationEnabled`](arbodytrackingconfiguration/automaticskeletonscaleestimationenabled.md) to [`true`](https://developer.apple.com/documentation/Swift/true) on [`ARBodyTrackingConfiguration`](arbodytrackingconfiguration.md), ARKit sets this property to a value between 0.0 and 1.0.

ARKit must know the height of a person in the camera feed to estimate an accurate world position for the person’s body anchor. ARKit uses the value of [`estimatedScaleFactor`](arbodyanchor/estimatedscalefactor.md) to correct the body anchor’s position in the physical environment.

The default body is 1.8 meters tall.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodyanchor/estimatedscalefactor)*