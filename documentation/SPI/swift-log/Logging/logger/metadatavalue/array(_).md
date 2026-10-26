---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/array(_:)"
framework: "swift-log/Logging"
---

# Logger.MetadataValue.array(_:)

**Framework**: swift-log/Logging  
**Kind**: case  
**Role**: Case

An array of metadata values.

## Declaration

```swift
case array([Metadata.Value])
```

#### Discussion

Because `MetadataValue` implements `ExpressibleByArrayLiteral`, you don’t need to type `.array([.string("foo"), .string("bar \(buz)")])`, instead use the more natural `["foo", "bar \(buz)"]`.

## See Also

### Types of metadata values
- [Logger.MetadataValue.string(_:)](./string%28_%29.md)
  A string metadata value.
- [case stringConvertible(any CustomStringConvertible & Sendable)](./stringconvertible%28_%29.md)
  A metadata value that conforms to custom string convertible.
- [Logger.MetadataValue.dictionary(_:)](./dictionary%28_%29.md)
  A metadata value which is a dictionary keyed with strings and storing metadata values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/array(_:))*