# MTLHazardTrackingMode.untracked

**Framework**: Metal  
**Kind**: case

An option specifying that the app must prevent hazards when modifying this object’s contents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case untracked
```

#### Discussion

Metal does not do any dependency analysis on untracked resources. You are responsible for ensuring that resources are modified safely. See [`Resource Synchronization`](resource-synchronization.md). When you already have detailed knowledge of how your app works, using untracked resources can improve performance.

## See Also

- [MTLHazardTrackingMode.default](mtlhazardtrackingmode/default.md)
  An option specifying that the default tracking mode should be used.
- [MTLHazardTrackingMode.tracked](mtlhazardtrackingmode/tracked.md)
  An option specifying that Metal prevents hazards when modifying this object’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlhazardtrackingmode/untracked)*