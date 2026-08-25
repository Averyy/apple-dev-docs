# attachedMode(of:)

**Framework**: Core Video  
**Kind**: method

Returns the propagation mode of a stored attachment you identify with a key path to a key definition that supplies a default, without retrieving it.

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
func attachedMode(of keyPath: KeyPath<Keys.Type, CVAttachmentKeyDefinitionWithDefault<some CVAttachmentModePreference, some CVAttachmentValueRepresentable & Equatable & Sendable>>) -> CVAttachmentMode?
```

#### Return Value

The propagation mode of the attachment, or `nil` if the key isn’t attached.

#### Discussion

Use this method to check for the presence of a specific key without converting its value.

Because this kind of key supplies a default, reading it as a property always produces a value, whether or not the container holds an attachment for it. This method returns `nil` in the second case, which makes it the way to tell a stored value from a defaulted one.

## Parameters

- `keyPath`: A key path to a key definition that supplies a default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer/attachedmode(of:)-7vger)*