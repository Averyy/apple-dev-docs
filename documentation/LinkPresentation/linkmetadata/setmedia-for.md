# setMedia(_:for:)

**Framework**: Link Presentation  
**Kind**: method

Sets the media data in the metadata for an attachment.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
mutating func setMedia(_ media: some Transferable, for attachment: LinkMetadata.Attachment)
```

#### Discussion

For example, a custom image can be set on some metadata:

```swift
metadata.setMedia(myImage, for: .image)
```

## Parameters

- `media`: The value to use for the media that corresponds to the specified attachment.
- `attachment`: The kind of attachment to modify, such as `.image`, `.icon`, and `.video`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/setmedia(_:for:))*