# JSONSerialization.WritingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSJSONWritingOptions : NSUInteger;
```

## Topics

### Creating a Writing Options Instance
- [init(rawValue: UInt)](./writingoptions/init%28rawvalue%29.md)
  Creates a set of JSON formatting options from an integer that represents those options.
### Formatting JSON
- [static var fragmentsAllowed: JSONSerialization.WritingOptions](./writingoptions/fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var prettyPrinted: JSONSerialization.WritingOptions](./writingoptions/prettyprinted.md)
  Specifies that the output uses white space and indentation to make the resulting data more readable.
- [static var sortedKeys: JSONSerialization.WritingOptions](./writingoptions/sortedkeys.md)
  Specifies that the output sorts keys in lexicographic order.
- [static var withoutEscapingSlashes: JSONSerialization.WritingOptions](./writingoptions/withoutescapingslashes.md)
  Specifies that the output doesn’t prefix slash characters with escape characters.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating JSON Data
- [class func data(withJSONObject: Any, options: JSONSerialization.WritingOptions) throws -> Data](./data%28withjsonobject,options%29.md)
  Returns JSON data from a Foundation object.
- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](./writejsonobject%28_,to,options,error%29.md)
  Writes a given JSON object to a stream.
- [class func isValidJSONObject(Any) -> Bool](./isvalidjsonobject%28_%29.md)
  Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions)*