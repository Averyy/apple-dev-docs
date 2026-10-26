---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/attributes"
framework: "swift-log/Logging"
---

# attributes

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

The attributes associated with this metadata value, if any.

## Declaration

```swift
var attributes: Logger.MetadataValueAttributes { get set }
```

#### Discussion

**Getting:** When the value is a [`Logger.MetadataValue.stringConvertible(_:)`](./stringconvertible%28_%29.md) wrapping an `AttributedStringCarrier`, returns that carrier’s attributes. For all other cases returns empty attributes.

**Setting:** Replaces the value with `.stringConvertible(AttributedStringCarrier(...))` carrying the given attributes. For `.string` and `.stringConvertible` cases the string representation is preserved. Setting attributes on a `.dictionary` or `.array` value is a programmer error: it triggers an assertion in debug builds and leaves the value unchanged in release builds. Set attributes on the leaf values instead.

Only handlers that inspect attributes pay the cost of the getter check.

## See Also

### Working with attributes
- [static func attributed(some CustomStringConvertible & Sendable, attributes: Logger.MetadataValueAttributes) -> Logger.MetadataValue](./attributed%28_,attributes%29.md)
  Creates an attributed metadata value from a string-convertible value and attributes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/attributes)*