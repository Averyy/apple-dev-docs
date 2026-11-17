# addVideoToSlide

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds a video to a slide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var addVideoToSlide: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `presentation` domain and one of your app’s actions matches the `addVideoToSlide` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .presentation.addVideoToSlide)` Swift macro.

The following example shows an intent that conforms to the `addVideoToSlide` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `presentation_addVideoToSlide` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .presentation.addVideoToSlide)
struct AddVideoToPresentationSlideIntent {
    /// Video to add.
    var video: IntentFile

    /// Slide to add the video to.
    var target: <#PresentationSlideEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the add-video-to-slide intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `video` | `IntentFile` | App Intents | Video to add. |
| `target` | `@AppEntity(schema: .presentation.slide)` | Your app | Slide to add the video to. `PresentationSlideEntity` is a placeholder name for a type that conforms to the [`slide`](../presentationentity/slide.md) entity schema, which your app defines and implements. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent/addvideotoslide)*