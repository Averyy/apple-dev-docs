# AssistantEnum

**Framework**: App Intents  
**Kind**: protocol

A value that Siri uses to fulfill a person’s request.

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

Don’t adopt this protocol directly, instead use the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro to meet requirements for making your [`AppEnum`](appenum.md) available to Siri.

## Relationships

### Inherits From
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantSchemaEnum](assistantschemaenum.md)

## See Also

- [protocol AssistantIntent](assistantintent.md)
  An app intent that Siri performs to fulfill a person’s request.
- [protocol AssistantSchemaIntent](assistantschemaintent.md)
- [protocol AssistantEntity](assistantentity.md)
  An app entity that Siri can access to fulfill a person’s request.
- [protocol AssistantSchemaEntity](assistantschemaentity.md)
- [protocol AssistantSchemaEnum](assistantschemaenum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantenum)*