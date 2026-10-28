# MTLResourceHazardTrackingModeDefault

**Framework**: Metal  
**Kind**: case  
**Role**: Enumeration Case

An option specifying that the default tracking mode should be used.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```c
MTLResourceHazardTrackingModeDefault
```

## Discussion

For more information, see [`MTLHazardTrackingMode.default`](../mtlhazardtrackingmode/default.md).

## See Also

### Specifying hazard tracking
- [static var hazardTrackingModeTracked: MTLResourceOptions](./hazardtrackingmodetracked.md)
  An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.
- [static var hazardTrackingModeUntracked: MTLResourceOptions](./hazardtrackingmodeuntracked.md)
  A resource option that instructs Metal to ignore memory hazards for a resource at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodedefault)*