# CVAttachmentContainer

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Provides storage for buffer attachments independent of the buffer lifetime

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
@dynamicMemberLookup
struct CVAttachmentContainer<Keys> where Keys : CVAttachmentKeyDefinitions
```

#### Overview

This object can be used to hold a copy of all buffer attachments. The attachment values can be accessed as properties of this object similar to [`CVAttachmentAccess`](./cvattachmentaccess.md).

## Topics

### Initializers
- [init(propagated: [String : any CVAttachmentValueRepresentable], nonPropagated: [String : any CVAttachmentValueRepresentable])](./cvattachmentcontainer/init%28propagated,nonpropagated%29.md)
### Instance Methods
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinition<some CVAttachmentModePreference, some CVAttachmentValueRepresentable>>) -> CVAttachmentMode?](./cvattachmentcontainer/attachedmode%28of%29-4qvrl.md)
  Returns the propagation mode of a stored attachment you identify with a key path to a key definition, without retrieving the value.
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<some CVAttachmentModePreference, some CVAttachmentValueRepresentable & Equatable & Sendable>>) -> CVAttachmentMode?](./cvattachmentcontainer/attachedmode%28of%29-7vger.md)
  Returns the propagation mode of a stored attachment you identify with a key path to a key definition that supplies a default, without retrieving it.
- [func attachedMode(of: String) -> CVAttachmentMode?](./cvattachmentcontainer/attachedmode%28of%29-p6ms.md)
  Returns the propagation mode of a stored attachment you identify by its raw key string, without retrieving the value.
- [func removeAll()](./cvattachmentcontainer/removeall%28%29.md)
  Removes all attachments.
- [func update(from: CVAttachmentContainer<Keys>)](./cvattachmentcontainer/update%28from%29.md)
  Updates propagated and non-propagated attachment values using the provided container.
### Subscripts
- [subscript<Value>(String, as _: Value.Type) -> (value: Value, mode: CVAttachmentMode)?](./cvattachmentcontainer/subscript%28_,as%29.md)
  Get or set attachment value associated with a string key
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinition<ModePreference, Value>>) -> Value?](./cvattachmentcontainer/subscript%28dynamicmember%29-3qlmo.md)
  Get or set attachment value as a property of this object.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<ModePreference, Value>>) -> Value](./cvattachmentcontainer/subscript%28dynamicmember%29-8zxr1.md)
  Get or set attachment value as a property of this object with default value.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentCompositeKeyDefinition<ModePreference, Value>>) -> Value?](./cvattachmentcontainer/subscript%28dynamicmember%29-fjtq.md)
  Get or set composite attachment value as a property of this object.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Attachment system (Swift)
- [struct CVAttachmentAccess](./cvattachmentaccess.md)
  Provides access to the attachments of a buffer.
- [struct CVAttachmentRawValue](./cvattachmentrawvalue.md)
  A lightweight wrapper around raw attachment values.
- [struct CVAttachmentKeyDefinition](./cvattachmentkeydefinition.md)
  Associates a raw attachment key with a value type and preferred propagation mode.
- [struct CVAttachmentKeyDefinitionWithDefault](./cvattachmentkeydefinitionwithdefault.md)
  Associates a raw attachment key with a default value and preferred propagation mode.
- [struct CVAttachmentCompositeKeyDefinition](./cvattachmentcompositekeydefinition.md)
  Associates a set of raw attachment keys with a value type and preferred propagation mode.
- [enum CVAttachmentModePreferenceShouldPropagate](./cvattachmentmodepreferenceshouldpropagate.md)
  Sets preferred mode for attachment to should propagate
- [enum CVAttachmentModePreferenceShouldNotPropagate](./cvattachmentmodepreferenceshouldnotpropagate.md)
  Sets preferred mode for attachment to should not propagate


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer)*