---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/dictionary(_:)"
framework: "swift-log/Logging"
---

# Logger.MetadataValue.dictionary(_:)

**Framework**: swift-log/Logging  
**Kind**: case  
**Role**: Case

A metadata value which is a dictionary keyed with strings and storing metadata values.

## Declaration

```swift
case dictionary(Metadata)
```

## Discussion

The type signature of the dictionary is `[String: Logger.MetadataValue]`.

Because `MetadataValue` implements `ExpressibleByDictionaryLiteral`, you don’t need to type `.dictionary(["foo": .string("bar \(buz)")])`, instead use the more natural `["foo": "bar \(buz)"]`.

## See Also

### Types of metadata values
- [Logger.MetadataValue.string(_:)](./string%28_%29.md)
  A string metadata value.
- [case stringConvertible(any CustomStringConvertible & Sendable)](./stringconvertible%28_%29.md)
  A metadata value that conforms to custom string convertible.
- [Logger.MetadataValue.array(_:)](./array%28_%29.md)
  An array of metadata values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/dictionary(_:))*