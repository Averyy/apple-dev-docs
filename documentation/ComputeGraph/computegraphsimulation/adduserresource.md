# addUserResource(_:)

**Framework**: Compute Graph  
**Kind**: method

Registers a resource for residency on all command encoders used by this simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
final func addUserResource(_ resource: any MTLResource)
```

#### Discussion

Only needed when buffers or textures are passed indirectly through structures using Metal Tier 2 Argument Buffers, since Metal cannot discover those resources automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/adduserresource(_:))*