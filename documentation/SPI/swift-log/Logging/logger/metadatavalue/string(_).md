---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/string(_:)"
framework: "swift-log/Logging"
---

# Logger.MetadataValue.string(_:)

**Framework**: swift-log/Logging  
**Kind**: case  
**Role**: Case

A string metadata value.

## Declaration

```swift
case string(String)
```

#### Discussion

Because `MetadataValue` implements `ExpressibleByStringInterpolation`, and `ExpressibleByStringLiteral`, you don’t need to type `.string(someType.description)` instead the string interpolation `"\(someType)"`.

## See Also

### Types of metadata values
- [case stringConvertible(any CustomStringConvertible & Sendable)](./stringconvertible%28_%29.md)
  A metadata value that conforms to custom string convertible.
- [Logger.MetadataValue.array(_:)](./array%28_%29.md)
  An array of metadata values.
- [Logger.MetadataValue.dictionary(_:)](./dictionary%28_%29.md)
  A metadata value which is a dictionary keyed with strings and storing metadata values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/string(_:))*