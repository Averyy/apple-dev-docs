# setUserResources(_:)

**Framework**: Compute Graph  
**Kind**: method

Sets additional resources for residency on all command buffers used by this simulation, replacing any previously added resources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func setUserResources(_ resources: [any MTLResource])
```

#### Discussion

Only needed when buffers or textures are passed indirectly through structures using Metal Tier 2 Argument Buffers, since Metal cannot discover those resources automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/setuserresources(_:))*