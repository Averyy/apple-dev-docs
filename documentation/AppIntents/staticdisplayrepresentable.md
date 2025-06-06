# StaticDisplayRepresentable

**Framework**: App Intents  
**Kind**: protocol

An interface for providing a static visual representation of a specific type.

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
protocol StaticDisplayRepresentable : CaseDisplayRepresentable, TypeDisplayRepresentable
```

## Relationships

### Inherits From
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AppEnum](appenum.md)
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
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
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/staticdisplayrepresentable)*