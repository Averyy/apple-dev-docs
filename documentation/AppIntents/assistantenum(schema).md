# AssistantEnum(schema:)

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

A Swift macro you use to make sure your app enum conforms to an assistant schema.

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
@attached(extension, conformances: AssistantSchemaEnum, names: named(__assistantSchemaEnum))
macro AssistantEnum<T>(schema: T) where T : AssistantSchemas.Enum
```

## See Also

### Deprecated macros
- [macro AssistantIntent<T>(schema: T)](./assistantintent%28schema%29.md)
  A Swift macro you use to make sure your app intent conforms to an assistant schema.
- [macro AssistantEntity<T>(schema: T)](./assistantentity%28schema%29.md)
  A Swift macro you use to make sure your app entity conforms to an assistant schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantenum(schema:))*