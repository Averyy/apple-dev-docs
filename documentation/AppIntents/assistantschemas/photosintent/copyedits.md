# copyEdits

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for copying edits to an asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var copyEdits: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.photos.copyEdits` schema:

```swift
@AppIntent(schema: .photos.copyEdits)
struct CopyMediaEditsIntent: AppIntent {
    @Parameter
    var name: String

    func perform() async throws -> some ReturnsValue<PhotoAlbumEntity> {
        .result(value: PhotoAlbumEntity())
    }
}
```

For more information about the `.photos` app intent domain, see doc:Making-photo-and-video-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosintent/copyedits)*