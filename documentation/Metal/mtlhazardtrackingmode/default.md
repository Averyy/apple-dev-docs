# MTLHazardTrackingMode.default

**Framework**: Metal  
**Kind**: case

An option that applies the default tracking behavior in Metal based on the resource or heap type you’re creating.

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

When you choose the [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md) option, Metal assigns a tracking mode based on the type you’re creating:

- The default tracking mode for an [`MTLHeap`](mtlheap.md) is [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) because heaps typically contain many resources that you manage manually.
- The default tracking mode for a type that inherits [`MTLResource`](mtlresource.md) is [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md) because individual resources benefit from automatic hazard tracking.

For example, Metal tracks hazards for [`MTLBuffer`](mtlbuffer.md) and [`MTLTexture`](mtltexture.md) instances when you create them with [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md).

For more information, see [`MTLHazardTrackingMode`](mtlhazardtrackingmode.md).

## See Also

- [MTLHazardTrackingMode.untracked](mtlhazardtrackingmode/untracked.md)
  An option that disables automatic memory hazard tracking in Metal for a resource at runtime.
- [MTLHazardTrackingMode.tracked](mtlhazardtrackingmode/tracked.md)
  An option that directs Metal to apply runtime safeguards that prevent memory hazards when commands access a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlhazardtrackingmode/default)*