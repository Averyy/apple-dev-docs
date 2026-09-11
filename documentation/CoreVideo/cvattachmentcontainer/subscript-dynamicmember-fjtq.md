# subscript(dynamicMember:)

**Framework**: Core Video  
**Kind**: subscript

Get or set composite attachment value as a property of this object.

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
subscript<ModePreference, Value>(dynamicMember keyPath: KeyPath<Keys.Type, CVAttachmentCompositeKeyDefinition<ModePreference, Value>>) -> Value? where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer/subscript(dynamicmember:)-fjtq)*