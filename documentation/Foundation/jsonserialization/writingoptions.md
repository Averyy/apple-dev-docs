# JSONSerialization.WritingOptions

**Framework**: Foundation  
**Kind**: struct

Options for writing JSON data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct WritingOptions
```

## Topics

### Creating a Writing Options Instance
- [init(rawValue: UInt)](jsonserialization/writingoptions/init(rawvalue:).md)
  Creates a set of JSON formatting options from an integer that represents those options.
### Formatting JSON
- [static var fragmentsAllowed: JSONSerialization.WritingOptions](jsonserialization/writingoptions/fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var prettyPrinted: JSONSerialization.WritingOptions](jsonserialization/writingoptions/prettyprinted.md)
  Specifies that the output uses white space and indentation to make the resulting data more readable.
- [static var sortedKeys: JSONSerialization.WritingOptions](jsonserialization/writingoptions/sortedkeys.md)
  Specifies that the output sorts keys in lexicographic order.
- [static var withoutEscapingSlashes: JSONSerialization.WritingOptions](jsonserialization/writingoptions/withoutescapingslashes.md)
  Specifies that the output doesn’t prefix slash characters with escape characters.
- [static var fragmentsAllowed: JSONSerialization.WritingOptions](jsonserialization/writingoptions/fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var prettyPrinted: JSONSerialization.WritingOptions](jsonserialization/writingoptions/prettyprinted.md)
  Specifies that the output uses white space and indentation to make the resulting data more readable.
- [static var sortedKeys: JSONSerialization.WritingOptions](jsonserialization/writingoptions/sortedkeys.md)
  Specifies that the output sorts keys in lexicographic order.
- [static var withoutEscapingSlashes: JSONSerialization.WritingOptions](jsonserialization/writingoptions/withoutescapingslashes.md)
  Specifies that the output doesn’t prefix slash characters with escape characters.

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

- [class func data(withJSONObject: Any, options: JSONSerialization.WritingOptions) throws -> Data](jsonserialization/data(withjsonobject:options:).md)
  Returns JSON data from a Foundation object.
- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](jsonserialization/writejsonobject(_:to:options:error:).md)
  Writes a given JSON object to a stream.
- [class func isValidJSONObject(Any) -> Bool](jsonserialization/isvalidjsonobject(_:).md)
  Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions)*