# AssistantIntent(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app intent conforms to an assistant schema.

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
(memberAttribute) @attached(extension, conformances: AssistantSchemaIntent, ShowInAppSearchResultsIntent, names: named(__assistantSchemaIntent)) macro AssistantIntent<T>(schema: T) where T : AssistantSchemas.Intent
```

## See Also

- [macro AssistantEntity<T>(schema: T)](assistantentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to an assistant schema.
- [macro AssistantEnum<T>(schema: T)](assistantenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to an assistant schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantintent(schema:))*