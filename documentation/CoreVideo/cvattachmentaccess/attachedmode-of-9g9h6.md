# attachedMode(of:)

**Framework**: Core Video  
**Kind**: method

Returns the propagation mode of an attachment you identify with a key path to a key definition, without retrieving the value.

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
func attachedMode(of keyPath: KeyPath<Keys.Type, CVAttachmentKeyDefinition<some CVAttachmentModePreference, some CVAttachmentValueRepresentable>>) -> CVAttachmentMode?
```

#### Return Value

The propagation mode of the attachment, or `nil` if the key isn’t attached.

#### Discussion

Use this method to check for the presence of a specific key without converting its value.

The mode this method returns is the mode the attachment actually carries, which can differ from the preferred mode the key definition declares. Code that sets an attachment through the key’s raw value can ignore that preference.

## Parameters

- `keyPath`: A key path to a key definition declared on the key definitions type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentaccess/attachedmode(of:)-9g9h6)*