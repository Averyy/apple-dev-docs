# AssistantEntity

**Framework**: App Intents  
**Kind**: protocol

An app entity that Siri can access to fulfill a person’s request.

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
protocol AssistantEntity : AppEntity
```

#### Overview

Don’t adopt this protocol directly, instead use the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro to meet requirements for making your [`AppEntity`](appentity.md) available to Siri.

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../Swift/Identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantSchemaEntity](assistantschemaentity.md)

## See Also

- [protocol AssistantIntent](assistantintent.md)
  An app intent that Siri performs to fulfill a person’s request.
- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantEnum](assistantenum.md)
  A value that Siri uses to fulfill a person’s request.
- [protocol AssistantSchemaEnum](assistantschemaenum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantentity)*