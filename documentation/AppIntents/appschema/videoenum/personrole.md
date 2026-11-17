# personRole

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a person role.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var personRole: some AppSchemaEnum { get }
```

## Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `video` domain and a parameter type matches the `personRole` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum(schema: .video.personRole)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `personRole` schema. You can create a type that conforms to the schema by adding the `@AppEnum` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `video_personRole` and select it from the code-completion suggestions:

```swift
@AppEnum(schema: .video.personRole)
enum VideoPersonRole: String {
    case actor
    case director
    case producer
    case writer
    case creator
    case executiveProducer
    case other

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .actor: "Actor",
        .director: "Director",
        .producer: "Producer",
        .writer: "Writer",
        .creator: "Creator",
        .executiveProducer: "Executive Producer",
        .other: "Other"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var imageType: some AppSchemaEnum](./imagetype.md)
  An enum schema for an image type.
- [var videoContentType: some AppSchemaEnum](./videocontenttype.md)
  An enum schema for a video content type.
- [AppSchema.VideoEnum](../videoenum.md)
  Identifies enum schemas in the video domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videoenum/personrole)*