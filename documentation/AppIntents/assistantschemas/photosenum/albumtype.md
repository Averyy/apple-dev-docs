# albumType

**Framework**: App Intents  
**Kind**: property

The type of photo album.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var albumType: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.photos.albumType` schema:

```swift
@AssistantEnum(schema: .photos.albumType)
enum PhotoAlbumType: AppEnum {
    case custom

    static var caseDisplayRepresentations: [PhotoAlbumType: AppIntents.DisplayRepresentation] = [
        .custom: "Custom",
    ]
}
```

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosenum/albumtype)*