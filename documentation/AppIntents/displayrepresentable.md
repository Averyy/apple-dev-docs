# DisplayRepresentable

**Framework**: App Intents  
**Kind**: protocol

An interface for providing a dynamic visual representation of a specific type and instances of that type.

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
protocol DisplayRepresentable : InstanceDisplayRepresentable, TypeDisplayRepresentable
```

## Relationships

### Inherits From
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AppEntity](appentity.md)
- [AssistantEntity](assistantentity.md)
- [AssistantSchemaEntity](assistantschemaentity.md)
- [FileEntity](fileentity.md)
- [IndexedEntity](indexedentity.md)
- [TransientAppEntity](transientappentity.md)
- [URLRepresentableEntity](urlrepresentableentity.md)
- [UniqueAppEntity](uniqueappentity.md)
### Conforming Types
- [IntentCurrencyAmount](intentcurrencyamount.md)
- [IntentFile](intentfile.md)
- [IntentPaymentMethod](intentpaymentmethod.md)
- [IntentPerson](intentperson.md)

## See Also

- [struct DisplayRepresentation](displayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [protocol TypeDisplayRepresentable](typedisplayrepresentable.md)
  An interface for providing the visual representation of a specific type.
- [struct TypeDisplayRepresentation](typedisplayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentable)*