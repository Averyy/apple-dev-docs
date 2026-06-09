# CVAttachmentRawValue

**Framework**: Core Video  
**Kind**: struct

A lightweight wrapper around raw attachment values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct CVAttachmentRawValue
```

#### Overview

This type encapsulates a raw attachment value and provides dictionary-like access to its content. The `subscript(key:)-(String)` allows access to internal values in a type safe way.

## Topics

### Initializers
- [init()](cvattachmentrawvalue/init.md)
  Creates an empty raw attachment value.
- [init(dictionaryLiteral: (String, (any CVAttachmentValueRepresentable)?)...)](cvattachmentrawvalue/init(dictionaryliteral:).md)
  Creates raw attachment value from dictionary literal.
### Subscripts
- [subscript<Value>(String, as _: Value.Type) -> Value?](cvattachmentrawvalue/subscript(_:as:).md)
  Get or set value associated with the specified key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)

## See Also

- [struct CVAttachmentAccess](cvattachmentaccess.md)
  Provides access to the attachments of a buffer.
- [struct CVAttachmentContainer](cvattachmentcontainer.md)
  Provides storage for buffer attachments independent of the buffer lifetime
- [struct CVAttachmentKeyDefinition](cvattachmentkeydefinition.md)
  Associates a raw attachment key with a value type and preferred propagation mode.
- [struct CVAttachmentKeyDefinitionWithDefault](cvattachmentkeydefinitionwithdefault.md)
  Associates a raw attachment key with a default value and preferred propagation mode.
- [struct CVAttachmentCompositeKeyDefinition](cvattachmentcompositekeydefinition.md)
  Associates a set of raw attachment keys with a value type and preferred propagation mode.
- [enum CVAttachmentModePreferenceShouldPropagate](cvattachmentmodepreferenceshouldpropagate.md)
  Sets preferred mode for attachment to should propagate
- [enum CVAttachmentModePreferenceShouldNotPropagate](cvattachmentmodepreferenceshouldnotpropagate.md)
  Sets preferred mode for attachment to should not propagate


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentrawvalue)*