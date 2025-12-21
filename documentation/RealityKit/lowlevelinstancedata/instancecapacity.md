# instanceCapacity

**Framework**: RealityKit  
**Kind**: property

The maximum number of instances this low-level instance data draws when set on a mesh instances component.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var instanceCapacity: Int { get }
```

#### Discussion

[`instanceCount`](lowlevelinstancedata/instancecount.md) must be less than or equal to the `instanceCapacity` determined on initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/instancecapacity)*