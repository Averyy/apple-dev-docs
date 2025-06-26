# instanceCapacity

**Framework**: RealityKit  
**Kind**: property

The current number of instances this LowLevelInstanceData will draw, when set on a MeshInstancesComponent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var instanceCapacity: Int { get }
```

#### Discussion

InstanceCount must be less than or equal to the instanceCapacity determined on initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/instancecapacity)*