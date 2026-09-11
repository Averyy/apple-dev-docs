# CVAttachmentCompositeKeyDefinition

**Framework**: Core Video  
**Kind**: struct

Associates a set of raw attachment keys with a value type and preferred propagation mode.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct CVAttachmentCompositeKeyDefinition<ModePreference, Value> where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable
```

#### Overview

The rawValues array should contain raw key strings required to represent any instance of Value. Even if some of the elements in rawValues are not required to represent certain instances of Value.

## Topics

### Initializers
- [init(String...)](cvattachmentcompositekeydefinition/init(_:).md)
### Instance Properties
- [var rawValues: [String]](cvattachmentcompositekeydefinition/rawvalues.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CVAttachmentAccess](cvattachmentaccess.md)
  Provides access to the attachments of a buffer.
- [struct CVAttachmentContainer](cvattachmentcontainer.md)
  Provides storage for buffer attachments independent of the buffer lifetime
- [struct CVAttachmentRawValue](cvattachmentrawvalue.md)
  A lightweight wrapper around raw attachment values.
- [struct CVAttachmentKeyDefinition](cvattachmentkeydefinition.md)
  Associates a raw attachment key with a value type and preferred propagation mode.
- [struct CVAttachmentKeyDefinitionWithDefault](cvattachmentkeydefinitionwithdefault.md)
  Associates a raw attachment key with a default value and preferred propagation mode.
- [enum CVAttachmentModePreferenceShouldPropagate](cvattachmentmodepreferenceshouldpropagate.md)
  Sets preferred mode for attachment to should propagate
- [enum CVAttachmentModePreferenceShouldNotPropagate](cvattachmentmodepreferenceshouldnotpropagate.md)
  Sets preferred mode for attachment to should not propagate


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcompositekeydefinition)*