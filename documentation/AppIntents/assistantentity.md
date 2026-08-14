# AssistantEntity

**Framework**: App Intents  
**Kind**: protocol

An app entity that Apple Intelligence can discover to fulfill a person’s request.

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
protocol AssistantEntity : AppEntity
```

#### Overview

Don’t adopt this protocol directly, instead use the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro to meet requirements for making your [`AppEntity`](appentity.md) discoverable by Apple Intelligence and Siri.

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../swift/identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantSchemaEntity](assistantschemaentity.md)

## See Also

- [protocol AssistantEnum](assistantenum.md)
  A value that Apple Intelligence and Siri use to fulfill a person’s request.
- [protocol AssistantIntent](assistantintent.md)
  An app intent that Siri performs to fulfill a person’s request.
- [protocol AssistantSchemaEnum](assistantschemaenum.md)
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [struct AssistantSchema](assistantschema.md)
- [enum AssistantSchemas](assistantschemas.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantentity)*