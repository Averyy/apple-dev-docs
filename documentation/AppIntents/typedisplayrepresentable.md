# TypeDisplayRepresentable

**Framework**: App Intents  
**Kind**: protocol

An interface for providing the visual representation of a specific type.

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
protocol TypeDisplayRepresentable
```

## Topics

### Type Properties
- [static var typeDisplayRepresentation: TypeDisplayRepresentation](typedisplayrepresentable/typedisplayrepresentation.md)
  A short, localized, human-readable name for the type.

## Relationships

### Inherited By
- [AppEntity](appentity.md)
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [AssistantEntity](assistantentity.md)
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEntity](assistantschemaentity.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [DisplayRepresentable](displayrepresentable.md)
- [FileEntity](fileentity.md)
- [IndexedEntity](indexedentity.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TransientAppEntity](transientappentity.md)
- [URLRepresentableEntity](urlrepresentableentity.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
- [UniqueAppEntity](uniqueappentity.md)
### Conforming Types
- [IntentCurrencyAmount](intentcurrencyamount.md)
- [IntentFile](intentfile.md)
- [IntentPaymentMethod](intentpaymentmethod.md)
- [IntentPerson](intentperson.md)
- [StringSearchScope](stringsearchscope.md)
- [VideoCategory](videocategory.md)

## See Also

- [struct DisplayRepresentation](displayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol DisplayRepresentable](displayrepresentable.md)
  An interface for providing a dynamic visual representation of a specific type and instances of that type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [struct TypeDisplayRepresentation](typedisplayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/typedisplayrepresentable)*