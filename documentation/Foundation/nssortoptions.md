# NSSortOptions

**Framework**: Foundation  
**Kind**: struct

Options for block sorting operations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSSortOptions
```

## Topics

### Constants
- [static var concurrent: NSSortOptions](nssortoptions/concurrent.md)
  Specifies that the Block sort operation should be concurrent.
- [static var stable: NSSortOptions](nssortoptions/stable.md)
  Specifies that the sorted results should return compared items having equal value in the order they occurred originally.
### Initializers
- [init(rawValue: UInt)](nssortoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class NSEnumerator](nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [protocol NSFastEnumeration](nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSEnumerationOptions](nsenumerationoptions.md)
  Options for block enumeration operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortoptions)*