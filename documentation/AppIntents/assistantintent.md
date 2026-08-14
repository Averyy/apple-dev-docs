# AssistantIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that Siri performs to fulfill a person’s request.

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
protocol AssistantIntent : AppIntent
```

#### Overview

Don’t adopt this protocol directly, instead use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro to meet requirements for making your [`AppIntent`](appintent.md) discoverable by Apple Intelligence and Siri.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Inherited By
- [AssistantSchemaIntent](assistantschemaintent.md)

## See Also

- [protocol AssistantEnum](assistantenum.md)
  A value that Apple Intelligence and Siri use to fulfill a person’s request.
- [protocol AssistantEntity](assistantentity.md)
  An app entity that Apple Intelligence can discover to fulfill a person’s request.
- [protocol AssistantSchemaEnum](assistantschemaenum.md)
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [struct AssistantSchema](assistantschema.md)
- [enum AssistantSchemas](assistantschemas.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantintent)*