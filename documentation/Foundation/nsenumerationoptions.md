# NSEnumerationOptions

**Framework**: Foundation  
**Kind**: struct

Options for block enumeration operations.

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
struct NSEnumerationOptions
```

## Topics

### Constants
- [static var concurrent: NSEnumerationOptions](nsenumerationoptions/concurrent.md)
  Specifies that the Block enumeration should be concurrent.
- [static var reverse: NSEnumerationOptions](nsenumerationoptions/reverse.md)
  Specifies that the enumeration should be performed in reverse.
### Initializers
- [init(rawValue: UInt)](nsenumerationoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [class NSEnumerator](nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [protocol NSFastEnumeration](nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSSortOptions](nssortoptions.md)
  Options for block sorting operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerationoptions)*