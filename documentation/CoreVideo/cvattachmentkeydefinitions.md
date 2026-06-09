# CVAttachmentKeyDefinitions

**Framework**: Core Video  
**Kind**: protocol

Marks a type as a collection of attachment keys for an attachment bearer.

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
protocol CVAttachmentKeyDefinitions
```

#### Overview

The static properties of a type which implements this protocol provide definitions for the attachment keys. The static properties which have one of [`CVAttachmentKeyDefinitions.Key`](cvattachmentkeydefinitions/key.md), [`CVAttachmentKeyDefinitions.KeyWithDefault`](cvattachmentkeydefinitions/keywithdefault.md) or [`CVAttachmentKeyDefinitions.CompositeKey`](cvattachmentkeydefinitions/compositekey.md) type are used by an attachment access provider to get and set attachment values.

For example, a custom attachment key for pixel buffers can be defined as:

```swift
extension CVPixelBufferAttachmentKeyDefinitions {
	// This extension makes the key available as a property of `pixelBuffer.attachments`.
	static var customAttachment: Key<ShouldPropagate, CustomAttachmentValue> {
		.init("com.myapp.customAttachmentKey")
	}
}

// This extension facilitates conversion between CustomAttachmentValue and CVAttachmentRawValue
extension CustomAttachmentValue: CVAttachmentValueRepresentable {
	static func makeFromRawAttachmentValue(_ repr: CVAttachmentRawValue) -> Self? {
		...
	}

	var rawAttachmentValueRepresentation: CVAttachmentRawValue {
		...
	}
}
```

## Topics

### Type Aliases
- [CVAttachmentKeyDefinitions.CompositeKey](cvattachmentkeydefinitions/compositekey.md)
- [CVAttachmentKeyDefinitions.Key](cvattachmentkeydefinitions/key.md)
- [CVAttachmentKeyDefinitions.KeyWithDefault](cvattachmentkeydefinitions/keywithdefault.md)
- [CVAttachmentKeyDefinitions.ShouldNotPropagate](cvattachmentkeydefinitions/shouldnotpropagate.md)
- [CVAttachmentKeyDefinitions.ShouldPropagate](cvattachmentkeydefinitions/shouldpropagate.md)

## Relationships

### Inherited By
- [CVImageBufferAttachmentKeyDefinitions](cvimagebufferattachmentkeydefinitions.md)
### Conforming Types
- [CVPixelBufferAttachmentKeyDefinitions](cvpixelbufferattachmentkeydefinitions.md)

## See Also

- [protocol CVBufferRepresentable](cvbufferrepresentable.md)
  CVBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVBuffer type.
- [protocol CVAttachmentModePreference](cvattachmentmodepreference.md)
  Defines preferred mode for an attachment key.
- [protocol CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
  Allows Swift types to be used as buffer attachment value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentkeydefinitions)*