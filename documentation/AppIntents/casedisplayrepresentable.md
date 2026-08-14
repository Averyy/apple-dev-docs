# CaseDisplayRepresentable

**Framework**: App Intents  
**Kind**: protocol

An interface for providing the visual representation for an iterable collection of values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
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
  A resource that helps provide a description of this instance.
- [var localizedStringResource: LocalizedStringResource](casedisplayrepresentable/localizedstringresource-78c15.md)
  A resource that helps provide a description of this instance.
### Default Implementations
- [CustomLocalizedStringResourceConvertible Implementations](casedisplayrepresentable/customlocalizedstringresourceconvertible-implementations.md)

## Relationships

### Inherits From
- [CaseIterable](../swift/caseiterable.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
### Inherited By
- [AppEnum](appenum.md)
- [AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
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