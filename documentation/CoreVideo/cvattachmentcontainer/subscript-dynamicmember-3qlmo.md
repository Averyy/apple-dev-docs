# subscript(dynamicMember:)

**Framework**: Core Video  
**Kind**: subscript

Get or set attachment value as a property of this object.

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
subscript<ModePreference, Value>(dynamicMember keyPath: KeyPath<Keys.Type, CVAttachmentKeyDefinition<ModePreference, Value>>) -> Value? where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer/subscript(dynamicmember:)-3qlmo)*