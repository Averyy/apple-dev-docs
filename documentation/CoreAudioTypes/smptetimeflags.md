# SMPTETimeFlags

**Framework**: Core Audio Types  
**Kind**: struct  
**Role**: Structure

A structure that defines SMPTE time flags.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct SMPTETimeFlags
```

```c
enum SMPTETimeFlags : UInt32;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./smptetimeflags/init%28rawvalue%29.md)
### Type Properties
- [static var running: SMPTETimeFlags](./smptetimeflags/running.md)
- [static var valid: SMPTETimeFlags](./smptetimeflags/valid.md)
### Constants
- [kSMPTETimeUnknown](./smptetimeflags/ksmptetimeunknown.md)

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

### SMPTE Time
- [struct SMPTETime](./smptetime.md)
  A structure that defines an SMPTE time value.
- [enum SMPTETimeType](./smptetimetype.md)
  Constants that define SMPTE time types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/smptetimeflags)*