---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/attributed(_:attributes:)"
framework: "swift-log/Logging"
---

# attributed(_:attributes:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Type Method

Creates an attributed metadata value from a string-convertible value and attributes.

## Declaration

```swift
static func attributed(_ value: some CustomStringConvertible & Sendable, attributes: Logger.MetadataValueAttributes) -> Logger.MetadataValue
```

## Discussion

This is a convenience factory that behaves like an additional enum case, producing a `.stringConvertible(AttributedStringCarrier(...))` value without string interpolation:

```swift
let value: Logger.MetadataValue = .attributed(userId, attributes: [Sensitivity.sensitive])
```

## See Also

### Working with attributes
- [var attributes: Logger.MetadataValueAttributes](./attributes.md)
  The attributes associated with this metadata value, if any.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/attributed(_:attributes:))*