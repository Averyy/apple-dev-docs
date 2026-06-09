# CVAttachmentAccess

**Framework**: Core Video  
**Kind**: struct

Provides access to the attachments of a buffer.

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
struct CVAttachmentAccess<Keys> where Keys : CVAttachmentKeyDefinitions
```

#### Overview

Lifetime of an instance of this type is tied to the lifetime of the buffer carrying attachments. The properties of this object are dynamically resolved to the static properties of the `Keys` type.

For example, when custom attachment keys are defined as follows:

```swift
extension CVImageBufferAttachmentKeyDefinitions {
	static var imageBufferName: Key<ShouldPropagate, String> {
		"com.app.imageBufferName"
	}
}
extension CVPixelBufferAttachmentKeyDefinitions {
	static var pixelBufferNumber: Key<ShouldPropagate, Int> {
		"com.app.pixelBufferNumber"
	}
}
```

Both keys can be accessed as a property of an CVAttachmentAccess instance. As CVImageBufferAttachmentKeyDefinitions is the superclass of CVPixelBufferAttachmentKeyDefinitions.

```swift
func inspect(attachments: borrowing CVAttachmentAccess<CVPixelBufferAttachmentKeyDefinitions>) {
	let value1: String? = attachments.imageBufferName
	let value2: Int? = attachments.pixelBufferNumber
}
```

It is also possible to access the keys by directly specifying raw string value:

```swift
let num: Int? = pixelBuffer.attachments["com.app.pixelBufferNumber"]
pixelBuffer.attachments["com.app.pixelBufferNumber"] = (100, .shouldPropagate)

// To set an attachment value by ignoring the preferred mode requires using rawValue of the key
pixelBuffer.attachments[CVPixelBufferAttachmentKeyDefinitions.displayDimensions.rawValue] = (CGSize(width: 600, height: 400), .shouldNotPropagate)
```

## Topics

### Instance Methods
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<some CVAttachmentModePreference, some CVAttachmentValueRepresentable & Equatable & Sendable>>) -> CVAttachmentMode?](cvattachmentaccess/attachedmode(of:)-79dr.md)
  Returns mode of an attached key without retriving value.
- [func attachedMode(of: KeyPath<Keys.Type, CVAttachmentKeyDefinition<some CVAttachmentModePreference, some CVAttachmentValueRepresentable>>) -> CVAttachmentMode?](cvattachmentaccess/attachedmode(of:)-9g9h6.md)
  Returns mode of an attached key without retriving value.
- [func attachedMode(of: String) -> CVAttachmentMode?](cvattachmentaccess/attachedmode(of:)-m49.md)
  Returns mode of an attached key without retriving value.
- [func copy() -> CVAttachmentContainer<Keys>](cvattachmentaccess/copy.md)
  Creates a copy all propagated and non-propagated attachments.
- [func propagate(from: borrowing CVAttachmentAccess<Keys>)](cvattachmentaccess/propagate(from:).md)
  Copies all propagated attachment values from another buffer.
- [func removeAll()](cvattachmentaccess/removeall.md)
  Removes all attachments.
- [func update(from: CVAttachmentContainer<Keys>)](cvattachmentaccess/update(from:).md)
  Updates propagated and non-propagated attachment values using the provided container.
### Subscripts
- [subscript<Value>(String, as _: Value.Type) -> (value: Value, mode: CVAttachmentMode)?](cvattachmentaccess/subscript(_:as:).md)
  Get or set attachment value associated with a string key
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentCompositeKeyDefinition<ModePreference, Value>>) -> Value?](cvattachmentaccess/subscript(dynamicmember:)-1ya6s.md)
  Get or set composite attachment value as a property of this object.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<ModePreference, Value>>) -> Value](cvattachmentaccess/subscript(dynamicmember:)-38ve9.md)
  Get or set attachment value as a property of this object with default value.
- [subscript<ModePreference, Value>(dynamicMember _: KeyPath<Keys.Type, CVAttachmentKeyDefinition<ModePreference, Value>>) -> Value?](cvattachmentaccess/subscript(dynamicmember:)-9egcs.md)
  Get or set attachment value as a property of this object.

## See Also

- [struct CVAttachmentContainer](cvattachmentcontainer.md)
  Provides storage for buffer attachments independent of the buffer lifetime
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentaccess)*