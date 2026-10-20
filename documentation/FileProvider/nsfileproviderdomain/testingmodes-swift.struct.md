# NSFileProviderDomain.TestingModes

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Modes that modify the system’s behavior while testing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
struct TestingModes
```

```c
enum NSFileProviderDomainTestingModes : NSUInteger;
```

## Topics

### Accessing Modes
- [static var alwaysEnabled: NSFileProviderDomain.TestingModes](./testingmodes-swift.struct/alwaysenabled.md)
  A testing mode that automatically enables the domain.
- [static var interactive: NSFileProviderDomain.TestingModes](./testingmodes-swift.struct/interactive.md)
  A testing mode where the extension can deterministically test asynchronous operations.
### Creating Modes
- [init(rawValue: UInt)](./testingmodes-swift.struct/init%28rawvalue%29.md)
  Returns a newly-created testing mode.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Testing
- [var testingModes: NSFileProviderDomain.TestingModes](./testingmodes-swift.property.md)
  A mode that gives the File Provider extension more control over the system’s behavior during testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/testingmodes-swift.struct)*