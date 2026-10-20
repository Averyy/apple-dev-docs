# NSEnumerationOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSEnumerationOptions : NSUInteger;
```

## Topics

### Constants
- [static var concurrent: NSEnumerationOptions](./nsenumerationoptions/concurrent.md)
  Specifies that the Block enumeration should be concurrent.
- [static var reverse: NSEnumerationOptions](./nsenumerationoptions/reverse.md)
  Specifies that the enumeration should be performed in reverse.
### Initializers
- [init(rawValue: UInt)](./nsenumerationoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Iteration
- [class NSEnumerator](./nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [protocol NSFastEnumeration](./nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](./nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](./nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSSortOptions](./nssortoptions.md)
  Options for block sorting operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerationoptions)*