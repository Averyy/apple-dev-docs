# NSDerivedAttributeDescription

**Framework**: Core Data  
**Kind**: class

A description of an attribute that derives its value by performing a calculation on a related attribute.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NSDerivedAttributeDescription
```

#### Overview

Use derived attributes to optimize fetch performance; for example:

- Create a derived `searchName` attribute to reflect a `name` attribute with case and diacritics removed for more efficient comparison.
- Create a derived `relationshipCount` attribute to reflect the number of objects in a relationship and avoid having to do a join.

Derived attributes support the following expressions:

|  |  |  |
| --- | --- | --- |
| to-one keypath | A single value to replicate. | `name` or `author.name` |
| to-one keypath with a function | The result of calling a function on a single value. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Supported functions include `canonical:`, `uppercase:`, and `lowercase:`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `canonical:` function returns a case- and diacritic-insensitive String value. | `canonical:(name)` |
| to-many keypath with a function | The result of calling an aggregate function on a set of values. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Supported functions include `@count` and `@sum`. | `friends.@count` |
| time | The current time. | `now()` |

> ❗ **Important**:  Data recomputes derived attributes when you save a context. A managed object’s property does not reflect unsaved changes until you save the context and refresh the object.

 Data recomputes derived attributes when you save a context. A managed object’s property does not reflect unsaved changes until you save the context and refresh the object.

## Topics

### Specifying the Derivation Expression
- [var derivationExpression: NSExpression?](nsderivedattributedescription/derivationexpression.md)
  An expression for generating derived data.

## Relationships

### Inherits From
- [NSAttributeDescription](nsattributedescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCompositeAttributeDescription](nscompositeattributedescription.md)
  A description of an attribute that derives its value by composing other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsderivedattributedescription)*