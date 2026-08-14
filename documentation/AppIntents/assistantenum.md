# AssistantEnum

**Framework**: App Intents  
**Kind**: protocol

A value that Apple Intelligence and Siri use to fulfill a person’s request.

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
protocol AssistantEnum : AppEnum
```

#### Overview

Don’t adopt this protocol directly, instead use the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro to meet requirements for making your [`AppEnum`](appenum.md) discoverable by Apple Intelligence and Siri.

## Relationships

### Inherits From
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../swift/caseiterable.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantSchemaEnum](assistantschemaenum.md)

## See Also

- [protocol AssistantEntity](assistantentity.md)
  An app entity that Apple Intelligence can discover to fulfill a person’s request.
- [protocol AssistantIntent](assistantintent.md)
  An app intent that Siri performs to fulfill a person’s request.
- [protocol AssistantSchemaEnum](assistantschemaenum.md)
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [struct AssistantSchema](assistantschema.md)
- [enum AssistantSchemas](assistantschemas.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantenum)*