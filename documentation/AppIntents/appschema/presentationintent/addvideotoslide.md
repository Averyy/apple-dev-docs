# addVideoToSlide

**Framework**: App Intents  
**Kind**: property

An intent schema that adds a video to a slide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var addVideoToSlide: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `presentation` domain and one of your app’s actions matches the `addVideoToSlide` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .presentation.addVideoToSlide)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `addVideoToSlide` schema:

```swift
@AppIntent(schema: .presentation.addVideoToSlide)
struct AddVideoToPresentationSlideIntent {
    var video: IntentFile
    var target: <#PresentationSlideEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent/addvideotoslide)*