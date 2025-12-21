# hazardTrackingModeUntracked

**Framework**: Metal  
**Kind**: property

A resource option that instructs Metal to ignore memory hazards for a resource at runtime.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var hazardTrackingModeUntracked: MTLResourceOptions { get }
```

#### Discussion

For more information, see [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md).

## See Also

- [static var hazardTrackingModeTracked: MTLResourceOptions](mtlresourceoptions/hazardtrackingmodetracked.md)
  An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/hazardtrackingmodeuntracked)*