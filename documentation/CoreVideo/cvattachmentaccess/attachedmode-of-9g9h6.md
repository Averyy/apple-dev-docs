# attachedMode(of:)

**Framework**: Core Video  
**Kind**: method

Returns mode of an attached key without retriving value.

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

#### Discussion

This function can be used to check for the presence of a specific key without converting it’s value. Returns `nil` if the key is not attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentaccess/attachedmode(of:)-9g9h6)*