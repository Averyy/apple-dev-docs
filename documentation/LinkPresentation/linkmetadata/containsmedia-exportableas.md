# containsMedia(_:exportableAs:)

**Framework**: Link Presentation  
**Kind**: method

Determines if a specific `Transferable` type can be loaded for an attachment in the metadata.

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
func containsMedia(_ attachment: LinkMetadata.Attachment, exportableAs type: (some Transferable).Type) -> Bool
```

#### Return Value

`true` if the metadata contains the specified attachment and the attachment’s content type is compatible with the media type.

#### Discussion

Use this function to immediately determine if metadata has some specific kind of media that can be coerced into a given type:

```swift
if metadata.containsMedia(.image, exportableAs: SwiftUI.Image.self) {
    // Load the image, and while waiting, display some loading indicator.
} else {
    // The metadata contains no image, so omit any UI for it.
}
```

## Parameters

- `attachment`: The kind of attachment to test, such as `.image`, `.icon`, and `.video`.
- `type`: The `Transferable` type of the media data to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/containsmedia(_:exportableas:))*