# configuration

**Framework**: Group Activities  
**Kind**: property

The current configuration of the system coordinator.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var configuration: SystemCoordinator.Configuration { get set }
```

#### Discussion

This property stores the [`SystemCoordinator`](systemcoordinator.md) object’s current support for displaying spatial Personas and placing them and your content in a shared simulation space. Assign a new value to this property to support spatial Personas and shared context in the current activity. The default configuration doesn’t enable support for these features.

## See Also

- [SystemCoordinator.Configuration](systemcoordinator/configuration-swift.struct.md)
  A structure that specifies your app’s support for activities that take place in a shared simulation space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/configuration-swift.property)*