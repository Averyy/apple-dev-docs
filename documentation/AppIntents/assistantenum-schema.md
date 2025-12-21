# AssistantEnum(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app enum conforms to an assistant schema.

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
(extension, conformances: AssistantSchemaEnum, names: named(__assistantSchemaEnum)) macro AssistantEnum<T>(schema: T) where T : AssistantSchemas.Enum
```

## See Also

- [macro AssistantIntent<T>(schema: T)](assistantintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an assistant schema.
- [macro AssistantEntity<T>(schema: T)](assistantentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to an assistant schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantenum(schema:))*