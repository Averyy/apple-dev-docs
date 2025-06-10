# AppEntity(schema:)

**Framework**: App Intents  
**Kind**: macro

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
(memberAttribute) @attached(extension, conformances: AppEntity, AssistantSchemaEntity, names: named(__assistantSchemaEntity)) macro AppEntity<T>(schema: T) where T : AssistantSchemas.Entity
```

## See Also

- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity(schema:))*