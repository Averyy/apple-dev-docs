# CVAttachmentContainer

**Framework**: Core Video  
**Kind**: struct

Provides storage for buffer attachments independent of the buffer lifetime

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
@dynamicMemberLookup
struct CVAttachmentContainer<Keys> where Keys : CVAttachmentKeyDefinitions
```

#### Overview

This object can be used to hold a copy of all buffer attachments. The attachment values can be accessed as properties of this object similar to [`CVAttachmentAccess`](cvattachmentaccess.md).

## Topics

### Initializers
- [init(propagated: [String : any CVAttachmentValueRepresentable], nonPropagated: [String : any CVAttachmentValueRepresentable])](cvattachmentcontainer/init(propagated:nonpropagated:).md)
### Instance Methods
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinition<some CVAttachmentModePreference, some CVAttachmentValueRepresentable>>) -> CVAttachmentMode?](cvattachmentcontainer/attachedmode(of:)-4qvrl.md)
  Returns mode of an attached key without retriving value.
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<some CVAttachmentModePreference, some CVAttachmentValueRepresentable & Equatable & Sendable>>) -> CVAttachmentMode?](cvattachmentcontainer/attachedmode(of:)-7vger.md)
  Returns mode of an attached key without retriving value.
- [func attachedMode(of: String) -> CVAttachmentMode?](cvattachmentcontainer/attachedmode(of:)-p6ms.md)
  Returns mode of an attached key without retriving value.
- [func removeAll()](cvattachmentcontainer/removeall.md)
  Removes all attachments.
- [func update(from: CVAttachmentContainer<Keys>)](cvattachmentcontainer/update(from:).md)
  Updates propagated and non-propagated attachment values using the provided container.
### Subscripts
- [subscript<Value>(String, as _: Value.Type) -> (value: Value, mode: CVAttachmentMode)?](cvattachmentcontainer/subscript(_:as:).md)
  Get or set attachment value associated with a string key
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinition<ModePreference, Value>>) -> Value?](cvattachmentcontainer/subscript(dynamicmember:)-3qlmo.md)
  Get or set attachment value as a property of this object.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<ModePreference, Value>>) -> Value](cvattachmentcontainer/subscript(dynamicmember:)-8zxr1.md)
  Get or set attachment value as a property of this object with default value.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentCompositeKeyDefinition<ModePreference, Value>>) -> Value?](cvattachmentcontainer/subscript(dynamicmember:)-fjtq.md)
  Get or set composite attachment value as a property of this object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CVAttachmentAccess](cvattachmentaccess.md)
  Provides access to the attachments of a buffer.
- [struct CVAttachmentRawValue](cvattachmentrawvalue.md)
  A lightweight wrapper around raw attachment values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer)*