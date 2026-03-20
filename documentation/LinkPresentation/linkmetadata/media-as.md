# media(_:as:)

**Framework**: Link Presentation  
**Kind**: method

Loads the media data of this metadata for an attachment as the specified Transferable type if possible.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
func media<Media>(_ attachment: LinkMetadata.Attachment, as type: Media.Type) async throws -> Media? where Media : Transferable
```

#### Return Value

A value of the `Transferable` type produced by the media data, or `nil` if there is no media data for the attachment as that type.

#### Discussion

For example, PNG image data can be extracted as a specific type from the metadata if available:

```swift
let value = try await metadata.media(.image, as: SwiftUI.Image.self) // `value` is a `SwiftUI.Image?`
```

## Parameters

- `attachment`: The kind of attachment to access, such as `.image`, `.icon`, and `.video`.
- `type`: The `Transferable` type to try to load the media data into. This type must support the content type of the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/media(_:as:))*