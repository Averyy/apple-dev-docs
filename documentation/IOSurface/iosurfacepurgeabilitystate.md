# IOSurfacePurgeabilityState

**Framework**: IOSurface  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct IOSurfacePurgeabilityState
```

```c
enum IOSurfacePurgeabilityState : uint32_t;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./iosurfacepurgeabilitystate/init%28rawvalue%29.md)
### Type Properties
- [static var purgeableEmpty: IOSurfacePurgeabilityState](./iosurfacepurgeabilitystate/purgeableempty.md)
- [static var purgeableKeepCurrent: IOSurfacePurgeabilityState](./iosurfacepurgeabilitystate/purgeablekeepcurrent.md)
- [static var purgeableVolatile: IOSurfacePurgeabilityState](./iosurfacepurgeabilitystate/purgeablevolatile.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Structures
- [struct IOSurfaceLockOptions](./iosurfacelockoptions.md)
- [struct IOSurfacePropertyKey](./iosurfacepropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacepurgeabilitystate)*