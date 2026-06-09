# label(_:)

**Framework**: Foundation Models  
**Kind**: method

Assigns a label to an attachment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func label(_ label: String) -> Attachment<Content>
```

## Mentions

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)

#### Discussion

Labels help the model identify specific attachments when making tool calls.

```swift
Attachment(image)
    .label("profile-photo")
```

## Parameters

- `label`: A string that identifies this attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/label(_:))*