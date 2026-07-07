# AppEntity(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app entity conforms to a schema.

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
(memberAttribute) @attached(extension, conformances: AppEntity, AssistantSchemaEntity, FileEntity, UniqueAppEntity, URLRepresentableEntity, names: named(__appSchemaEntity)) macro AppEntity<T>(schema: T) where T : AppSchemaEntity
```

## Mentions

- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)

## See Also

- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity(schema:))*