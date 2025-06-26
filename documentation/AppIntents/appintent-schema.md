# AppIntent(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app intent conforms to an schema.

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
@attached
(memberAttribute) @attached(extension, conformances: AppIntent, AssistantSchemaIntent, ShowInAppSearchResultsIntent, names: named(__assistantSchemaIntent)) macro AppIntent<T>(schema: T) where T : AssistantSchemas.Intent
```

## See Also

- [macro AppEntity<T>(schema: T)](appentity(schema:).md)
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent(schema:))*