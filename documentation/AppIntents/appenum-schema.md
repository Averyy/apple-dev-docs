# AppEnum(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app enum conforms to a schema.

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
(extension, conformances: AssistantSchemaEnum, names: named(__assistantSchemaEnum)) macro AppEnum<T>(schema: T) where T : AssistantSchemas.Enum
```

## See Also

- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEntity<T>(schema: T)](appentity(schema:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appenum(schema:))*