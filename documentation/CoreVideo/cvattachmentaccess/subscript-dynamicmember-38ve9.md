# subscript(dynamicMember:)

**Framework**: Core Video  
**Kind**: subscript

Get or set attachment value as a property of this object with default value.

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
subscript<ModePreference, Value>(dynamicMember keyPath: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<ModePreference, Value>>) -> Value where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable, Value : Equatable, Value : Sendable { get set }
```

#### Overview

This subscript provides access to an attachment key as a property. The key to be accessed must be defined as a static property on the `Keys` type.

```swift
extension CVPixelBufferAttachmentKeyDefinitions {
	static var isSpecialPicture: KeyWithDefault<ShouldPropagate, Bool> {
		.init("com.app.isSpecialPicture", default: false)
	}
}

func inspect(attachments: borrowing CVAttachmentAccess<CVPixelBufferAttachmentKeyDefinitions>) {
	if attachments.isSpecialPicture {
		...
	}
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentaccess/subscript(dynamicmember:)-38ve9)*