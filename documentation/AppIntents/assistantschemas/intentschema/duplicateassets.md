# duplicateAssets

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for duplicating an asset.

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
var duplicateAssets: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app intent that conforms to the `.photos.duplicateAssets` schema:

```swift
@AssistantIntent(schema: .photos.duplicateAssets)
struct DuplicateMediaAssetsIntent: AppIntent {
    @Parameter
    var entities: [PhotoEntity]

    func perform() async throws -> some ReturnsValue<[PhotoEntity]> {
        .result(value: [PhotoEntity()])
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/duplicateassets)*