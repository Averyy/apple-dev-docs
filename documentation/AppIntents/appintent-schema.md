# AppIntent(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app intent conforms to an schema.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@attached
(memberAttribute) @attached(extension, conformances: AppIntent, AssistantSchemaIntent, ShowInAppSearchResultsIntent, OpenIntent, DeleteIntent, AudioPlaybackIntent, AudioRecordingIntent, LiveActivityIntent, URLRepresentableIntent, names: named(__appSchemaIntent)) macro AppIntent<T>(schema: T) where T : AppSchemaIntent
```

## Mentions

- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)
- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)

## See Also

- [macro AppEntity<T>(schema: T)](appentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to a schema.
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent(schema:))*