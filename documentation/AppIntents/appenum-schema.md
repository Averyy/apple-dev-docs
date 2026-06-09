# AppEnum(schema:)

**Framework**: App Intents  
**Kind**: macro

A Swift macro you use to make sure your app enum conforms to a schema.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@attached
(extension, conformances: AppEnum, AssistantSchemaEnum, names: named(__appSchemaEnum)) macro AppEnum<T>(schema: T) where T : AppSchemaEnum
```

## Mentions

- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)

## See Also

- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEntity<T>(schema: T)](appentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appenum(schema:))*