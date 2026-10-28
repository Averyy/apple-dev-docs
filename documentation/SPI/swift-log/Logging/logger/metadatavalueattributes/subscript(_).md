---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/subscript(_:)"
framework: "swift-log/Logging"
---

# subscript(_:)

**Framework**: swift-log/Logging  
**Kind**: subscript  
**Role**: Instance Subscript

Get or set a custom attribute by its type.

## Declaration

```swift
subscript<Attr>(attribute: Attr.Type) -> Attr? where Attr : Logger.MetadataValueAttributes.Attribute { get set }
```

## Return Value

The attribute value, or `nil` if not set.

## Parameters

- `attribute`: The metatype of the attribute to access.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/subscript(_:))*