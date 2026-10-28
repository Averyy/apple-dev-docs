---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/init(stringinterpolation:)"
framework: "swift-log/Logging"
---

# init(stringInterpolation:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates a metadata value from string interpolation.

## Declaration

```swift
init(stringInterpolation: StringInterpolation)
```

## Discussion

If any interpolation segment specified attributes, the result is `.stringConvertible(AttributedStringCarrier(...))`. Otherwise, `.string(...)`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalue/init(stringinterpolation:))*