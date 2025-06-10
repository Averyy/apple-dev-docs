# AssistantIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that Siri performs to fulfill a person’s request.

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
protocol AssistantIntent : AppIntent
```

#### Overview

Don’t adopt this protocol directly, instead use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro to meet requirements for making your [`AppIntent`](appintent.md) available to Siri.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [AssistantSchemaIntent](assistantschemaintent.md)

## See Also

- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [protocol AssistantEntity](assistantentity.md)
  An app entity that Siri can access to fulfill a person’s request.
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantEnum](assistantenum.md)
  A value that Siri uses to fulfill a person’s request.
- [protocol AssistantSchemaEnum](assistantschemaenum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantintent)*