---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument"
framework: "swift-argument-parser/ArgumentParser"
---

# ExpressibleByArgument

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that can be expressed as a command-line argument.

## Declaration

```swift
protocol ExpressibleByArgument : _SendableMetatype
```

## Mentions

- [Customizing Help](./customizinghelp.md)
- [Customizing Completions](./customizingcompletions.md)
- [Declaring Arguments, Options, and Flags](./declaringarguments.md)

## Topics

### Initializers
- [init?(argument: String)](./expressiblebyargument/init%28argument%29.md)
  Creates a new instance of this type from a command-line-specified argument.
### Instance Properties
- [var defaultValueDescription: String](./expressiblebyargument/defaultvaluedescription.md)
  The description of this instance to show as a default value in a command-line tool’s help screen.
### Type Properties
- [static var allValueDescriptions: [String : String]](./expressiblebyargument/allvaluedescriptions.md)
  A dictionary containing the descriptions for each possible value of this type, for display in the help screen.
- [static var allValueStrings: [String]](./expressiblebyargument/allvaluestrings.md)
  An array of all possible strings that can convert to a value of this type, for display in the help screen.
- [static var defaultCompletionKind: CompletionKind](./expressiblebyargument/defaultcompletionkind.md)
  The completion kind to use for options or arguments of this type that don’t explicitly declare a completion kind.

## Relationships

### Inherits From
- Swift.SendableMetatype
### Conforming Types
- [Bool](./swift/bool.md)
- [Double](./swift/double.md)
- [Float](./swift/float.md)
- [Int](./swift/int.md)
- [Int16](./swift/int16.md)
- [Int32](./swift/int32.md)
- [Int64](./swift/int64.md)
- [Int8](./swift/int8.md)
- [String](./swift/string.md)
- [UInt](./swift/uint.md)
- [UInt16](./swift/uint16.md)
- [UInt32](./swift/uint32.md)
- [UInt64](./swift/uint64.md)
- [UInt8](./swift/uint8.md)

## See Also

### Custom Types
- [protocol EnumerableFlag](./enumerableflag.md)
  A type that represents the different possible flags to be used by a `@Flag` property.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument)*