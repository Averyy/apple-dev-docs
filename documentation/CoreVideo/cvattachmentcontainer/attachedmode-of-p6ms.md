# attachedMode(of:)

**Framework**: Core Video  
**Kind**: method

Returns the propagation mode of a stored attachment you identify by its raw key string, without retrieving the value.

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
func attachedMode(of key: String) -> CVAttachmentMode?
```

#### Return Value

The propagation mode of the attachment, or `nil` if the key isn’t attached.

#### Discussion

Use this method to check for the presence of a specific key without converting its value.

This overload takes the key as a string, which is how you reach an attachment whose key isn’t declared as a property of the key definitions type, such as a custom key your app attaches. To pass a declared key, use its [`rawValue`](cvattachmentkeydefinition/rawvalue.md).

## Parameters

- `key`: The raw string that identifies the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentcontainer/attachedmode(of:)-p6ms)*