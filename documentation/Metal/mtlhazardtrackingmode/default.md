# MTLHazardTrackingMode.default

**Framework**: Metal  
**Kind**: case

An option specifying that the default tracking mode should be used.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case `default`
```

#### Discussion

The default behavior varies depending on the type of object being tracked:

| Resource | [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md) |
| --- | --- |
| Heap | [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) |

## See Also

- [MTLHazardTrackingMode.untracked](mtlhazardtrackingmode/untracked.md)
  An option specifying that the app must prevent hazards when modifying this object’s contents.
- [MTLHazardTrackingMode.tracked](mtlhazardtrackingmode/tracked.md)
  An option specifying that Metal prevents hazards when modifying this object’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlhazardtrackingmode/default)*