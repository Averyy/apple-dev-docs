# TypeDisplayRepresentation

**Framework**: App Intents  
**Kind**: struct

A type that describes the user interface presentation of a custom type.

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
struct TypeDisplayRepresentation
```

## Topics

### Initializers
- [init(name: LocalizedStringResource, numericFormat: LocalizedStringResource?)](typedisplayrepresentation/init(name:numericformat:).md)
- [init(name: LocalizedStringResource, numericFormat: LocalizedStringResource?, synonyms: [LocalizedStringResource])](typedisplayrepresentation/init(name:numericformat:synonyms:).md)
### Instance Properties
- [var name: LocalizedStringResource](typedisplayrepresentation/name.md)
  The singular type name, e.g. “Book”.
- [var numericFormat: LocalizedStringResource?](typedisplayrepresentation/numericformat.md)
  A string representing a count for the type, e.g. “2 books”.
- [var synonyms: [LocalizedStringResource]](typedisplayrepresentation/synonyms.md)
  A list of localized phrases that are synonyms of this particular type display representation

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DisplayRepresentation](displayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol DisplayRepresentable](displayrepresentable.md)
  An interface for providing a dynamic visual representation of a specific type and instances of that type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [protocol TypeDisplayRepresentable](typedisplayrepresentable.md)
  An interface for providing the visual representation of a specific type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/typedisplayrepresentation)*