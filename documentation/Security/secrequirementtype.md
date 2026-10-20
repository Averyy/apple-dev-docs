# SecRequirementType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

An enumeration indicating different types of internal requirements for code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecRequirementType
```

```c
enum SecRequirementType : uint32_t;
```

#### Overview

These constants are indexes into requirement sets and are not currently used in any public API.

## Topics

### Constants
- [SecRequirementType.hostRequirementType](./secrequirementtype/hostrequirementtype.md)
  What hosts may run this code.
- [SecRequirementType.guestRequirementType](./secrequirementtype/guestrequirementtype.md)
  What guests this code may run.
- [SecRequirementType.designatedRequirementType](./secrequirementtype/designatedrequirementtype.md)
  A designated requirement.
- [SecRequirementType.libraryRequirementType](./secrequirementtype/libraryrequirementtype.md)
  What libraries this code may link against.
- [SecRequirementType.pluginRequirementType](./secrequirementtype/pluginrequirementtype.md)
  What plug-ins this code may load.
- [SecRequirementType.invalidRequirementType](./secrequirementtype/invalidrequirementtype.md)
  Invalid type of requirement.
- [static var requirementTypeCount: SecRequirementType](./secrequirementtype/requirementtypecount.md)
  The number of valid requirement types.
### Initializers
- [init?(rawValue: UInt32)](./secrequirementtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementtype)*