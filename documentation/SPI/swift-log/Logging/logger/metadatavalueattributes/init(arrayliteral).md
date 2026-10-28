---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/init(arrayliteral:)"
framework: "swift-log/Logging"
---

# init(arrayLiteral:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates metadata value attributes from an array literal of attribute values.

## Declaration

```swift
init(arrayLiteral elements: any Logger.MetadataValueAttributes.Attribute...)
```

## Discussion

Each element is any [`Logger.MetadataValueAttributes.Attribute`](./attribute.md) conforming value. The key is inferred from the concrete type of the value.

```swift
let attrs: Logger.MetadataValueAttributes = [Sensitivity.sensitive, ValueType.int64]
```

Each element goes through existential boxing to extract `type(of:)` and `.rawValue`. This is acceptable for a literal initializer but should not be used in hot paths; prefer the type-safe subscript (`attrs[SomeAttribute.self] = value`) for performance-sensitive code.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/init(arrayliteral:))*