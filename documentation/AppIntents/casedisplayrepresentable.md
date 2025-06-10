# CaseDisplayRepresentable

**Framework**: App Intents  
**Kind**: protocol

An interface for providing the visual representation for an iterable collection of values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol CaseDisplayRepresentable : CustomLocalizedStringResourceConvertible, CaseIterable, Hashable
```

## Topics

### Describing the case conditions
- [static var caseDisplayRepresentations: [Self : DisplayRepresentation]](casedisplayrepresentable/casedisplayrepresentations.md)
  A dictionary that maps each value to the visual elements that represent it.
### Providing a localized description
- [var localizedStringResource: LocalizedStringResource](casedisplayrepresentable/localizedstringresource-7gj71.md)
- [var localizedStringResource: LocalizedStringResource](casedisplayrepresentable/localizedstringresource-78c15.md)

## Relationships

### Inherits From
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Inherited By
- [AppEnum](appenum.md)
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
### Conforming Types
- [StringSearchScope](stringsearchscope.md)
- [VideoCategory](videocategory.md)

## See Also

- [struct DisplayRepresentation](displayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol DisplayRepresentable](displayrepresentable.md)
  An interface for providing a dynamic visual representation of a specific type and instances of that type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [protocol TypeDisplayRepresentable](typedisplayrepresentable.md)
  An interface for providing the visual representation of a specific type.
- [struct TypeDisplayRepresentation](typedisplayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/casedisplayrepresentable)*