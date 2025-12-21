# MTLHazardTrackingMode.untracked

**Framework**: Metal  
**Kind**: case

An option that disables automatic memory hazard tracking in Metal for a resource at runtime.

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

Create resources with this option when you’re managing resource synchronization. Metal doesn’t track memory dependencies for untracked resources, which means you’re responsible for ensuring that commands access those resources safely with barriers, fences, or events.

Untracked resources can improve runtime performance when you have detailed knowledge of how your app manages resource dependencies and can manually synchronize access more efficiently than with automatic tracking in Metal.

For more information about hazard tracking and synchronization trade-offs, see [`MTLHazardTrackingMode`](mtlhazardtrackingmode.md).

## See Also

- [MTLHazardTrackingMode.default](mtlhazardtrackingmode/default.md)
  An option that applies the default tracking behavior in Metal based on the resource or heap type you’re creating.
- [MTLHazardTrackingMode.tracked](mtlhazardtrackingmode/tracked.md)
  An option that directs Metal to apply runtime safeguards that prevent memory hazards when commands access a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlhazardtrackingmode/untracked)*