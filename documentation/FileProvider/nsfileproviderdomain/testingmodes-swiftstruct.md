# NSFileProviderDomain.TestingModes

**Framework**: File Provider  
**Kind**: struct

Modes that modify the system’s behavior while testing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
struct TestingModes
```

## Topics

### Accessing Modes
- [static var alwaysEnabled: NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.struct/alwaysenabled.md)
  A testing mode that automatically enables the domain.
- [static var interactive: NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.struct/interactive.md)
  A testing mode where the extension can deterministically test asynchronous operations.
### Creating Modes
- [init(rawValue: UInt)](nsfileproviderdomain/testingmodes-swift.struct/init(rawvalue:).md)
  Returns a newly-created testing mode.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var testingModes: NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.property.md)
  A mode that gives the File Provider extension more control over the system’s behavior during testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/testingmodes-swift.struct)*