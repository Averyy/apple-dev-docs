# subscript(dynamicMember:)

**Framework**: Core Video  
**Kind**: subscript

Get or set composite attachment value as a property of this object.

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
subscript<ModePreference, Value>(dynamicMember keyPath: KeyPath<Keys.Type, CVAttachmentCompositeKeyDefinition<ModePreference, Value>>) -> Value? where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable { get set }
```

#### Overview

This subscript provides access to an attachment key as a property. The key to be accessed must be defined as a static property on the `Keys` type. This accessor is intended to be used with legacy keys which are not grouped together in a single container. For new keys, use [`CVAttachmentKeyDefinitions.Key`](cvattachmentkeydefinitions/key.md) instead of using a composite key group.

```swift
enum MyImageTag: CVAttachmentValueRepresentable {
	case int(Int)
	case string(String)

	static func makeFromRawAttachmentValue(_ repr: CVAttachmentRawValue) -> Self? {
		guard let kind: String = repr["com.app.MyImageTag.Kind"] else { return nil }
		switch kind {
		case "int":
			guard let value: Int = repr["com.app.MyImageTag.Value"] else { return nil }
			return .int(value)
		case "str":
			guard let value: String = repr["com.app.MyImageTag.Value"] else { return nil }
			return .string(value)
		default:
			return nil
		}
	}

	var rawAttachmentValueRepresentation: CVAttachmentRawValue {
		switch self {
		case .int(let value):
			[
				"com.app.MyImageTag.Kind": "int",
				"com.app.MyImageTag.Value": value,
			]
		case .string(let value):
			[
				"com.app.MyImageTag.Kind": "str",
				"com.app.MyImageTag.Value": value,
			]
		}
	}
}

extension CVPixelBufferAttachmentKeyDefinitions {
	/// A composite key definition which combines legacy top level raw keys
	static var myLegacyImageTag: CompositeKey<ShouldPropagate, MyImageTag> {
		["com.app.MyImageTag.Kind", "com.app.MyImageTag.Value"]
	}

	/// For new code, a single key should be used
	static var myImageTag: Key<ShouldPropagate, MyImageTag> {
		"com.app.MyImageTag"
	}
}

func inspect(attachments: borrowing CVAttachmentAccess<CVPixelBufferAttachmentKeyDefinitions>) {
	let value1: MyImageTag? = attachments.myLegacyImageTag
	let value2: MyImageTag? = attachments.myImageTag
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentaccess/subscript(dynamicmember:)-1ya6s)*