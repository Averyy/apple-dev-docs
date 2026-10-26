---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue"
framework: "swift-log/Logging"
---

# Logger.MetadataValue

**Framework**: swift-log/Logging  
**Kind**: enum  
**Role**: Enumeration

A logging metadata value.

## Declaration

```swift
enum MetadataValue
```

#### Overview

`Logger.MetadataValue` is a string, array, or a dictionary literal convertible.

`MetadataValue` provides convenient conformances to `ExpressibleByStringInterpolation`, `ExpressibleByStringLiteral`, `ExpressibleByArrayLiteral`, and `ExpressibleByDictionaryLiteral` which means that when constructing `MetadataValue`s you should default to using Swift’s usual literals.

Prefer using string interpolation for convenience, for example:

```swift
logger.info(
    "user logged in",
    metadata: ["user-id": "\(user.id)"]
)
```

over:

```swift
logger.info(
    "user logged in",
    metadata: ["user-id": .string(user.id.description)]
)
```

Rather than explicitly asserting that the metadata is an array or dictionary, use the string literal to interpolate into the result:

```swift
logger.info(
    "user selected colors",
    metadata: ["colors": ["\(user.topColor)", "\(user.secondColor)"]])
```

over:

```swift
logger.info(
    "user selected colors",
    metadata: [
        "colors": .array([.string("\(user.topColor)"), .string("\(user.secondColor)")
    ]
)
```

and an example that illustrates presenting a dictionary:

```swift
logger.info(
    "nested info",
    metadata: [
      "nested": [
        "fave-numbers": ["\(1)", "\(2)", "\(3)"],
        "foo": "bar"
      ]
    ]
)
```

over

```swift
logger.info(
    "nested info",
    metadata: [
      "nested": .dictionary([
        "fave-numbers": ["\(1)", "\(2)", "\(3)"],
        "foo": "bar"
      ])
])
```

## Topics

### Types of metadata values
- [Logger.MetadataValue.string(_:)](./metadatavalue/string%28_%29.md)
  A string metadata value.
- [case stringConvertible(any CustomStringConvertible & Sendable)](./metadatavalue/stringconvertible%28_%29.md)
  A metadata value that conforms to custom string convertible.
- [Logger.MetadataValue.array(_:)](./metadatavalue/array%28_%29.md)
  An array of metadata values.
- [Logger.MetadataValue.dictionary(_:)](./metadatavalue/dictionary%28_%29.md)
  A metadata value which is a dictionary keyed with strings and storing metadata values.
### Working with attributes
- [static func attributed(some CustomStringConvertible & Sendable, attributes: Logger.MetadataValueAttributes) -> Logger.MetadataValue](./metadatavalue/attributed%28_,attributes%29.md)
  Creates an attributed metadata value from a string-convertible value and attributes.
- [var attributes: Logger.MetadataValueAttributes](./metadatavalue/attributes.md)
  The attributes associated with this metadata value, if any.
### Default Implementations
- [CustomStringConvertible Implementations](./metadatavalue/customstringconvertible-implementations.md)
- [Equatable Implementations](./metadatavalue/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](./metadatavalue/expressiblebyarrayliteral-implementations.md)
- [ExpressibleByDictionaryLiteral Implementations](./metadatavalue/expressiblebydictionaryliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./metadatavalue/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](./metadatavalue/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](./metadatavalue/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByDictionaryLiteral
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringInterpolation
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Adjusting logger metadata
- [subscript(metadataKey _: String) -> Logger.Metadata.Value?](./subscript%28metadatakey%29.md)
  Log a message using the log level and attributed metadata that you provide.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue)*