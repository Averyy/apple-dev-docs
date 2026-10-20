# JSONSerialization.ReadingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options used when creating Foundation objects from JSON data.

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
struct ReadingOptions
```

```c
enum NSJSONReadingOptions : NSUInteger;
```

#### Overview

Use these options when parsing JSON with [`jsonObject(with:options:)`](./jsonobject%28with,options%29-8demi.md) and [`jsonObject(with:options:)`](./jsonobject%28with,options%29-3afap.md).

## Topics

### Creating a Reading Options Instance
- [init(rawValue: UInt)](./readingoptions/init%28rawvalue%29.md)
  Creates a set of JSON formatting options from an integer that represents those options.
### Reading Options
- [static var mutableContainers: JSONSerialization.ReadingOptions](./readingoptions/mutablecontainers.md)
  Specifies that arrays and dictionaries in the returned object are mutable.
- [static var mutableLeaves: JSONSerialization.ReadingOptions](./readingoptions/mutableleaves.md)
  Specifies that leaf strings in the JSON object graph are mutable.
- [static var fragmentsAllowed: JSONSerialization.ReadingOptions](./readingoptions/fragmentsallowed.md)
  Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [static var json5Allowed: JSONSerialization.ReadingOptions](./readingoptions/json5allowed.md)
  Specifies that reading serialized JSON data supports the JSON5 syntax.
- [static var topLevelDictionaryAssumed: JSONSerialization.ReadingOptions](./readingoptions/topleveldictionaryassumed.md)
  Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
- [static var allowFragments: JSONSerialization.ReadingOptions](./readingoptions/allowfragments.md)
  A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.

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

### Creating a JSON Object
- [class func jsonObject(with: Data, options: JSONSerialization.ReadingOptions) throws -> Any](./jsonobject%28with,options%29-8demi.md)
  Returns a Foundation object from given JSON data.
- [class func jsonObject(with: InputStream, options: JSONSerialization.ReadingOptions) throws -> Any](./jsonobject%28with,options%29-3afap.md)
  Returns a Foundation object from JSON data in a given stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions)*