# hazardTrackingModeTracked

**Framework**: Metal  
**Kind**: property

An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var hazardTrackingModeTracked: MTLResourceOptions { get }
```

#### Discussion

For more information, see [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).

## See Also

- [static var hazardTrackingModeUntracked: MTLResourceOptions](mtlresourceoptions/hazardtrackingmodeuntracked.md)
  A resource option that instructs Metal to ignore memory hazards for a resource at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/hazardtrackingmodetracked)*