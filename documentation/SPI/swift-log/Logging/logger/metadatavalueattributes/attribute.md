---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/attribute"
framework: "swift-log/Logging"
---

# Logger.MetadataValueAttributes.Attribute

**Framework**: swift-log/Logging  
**Kind**: protocol  
**Role**: Protocol

A protocol for defining custom metadata attributes.

## Declaration

```swift
protocol Attribute : RawRepresentable, Sendable where Self.RawValue == Int64
```

## Overview

Conform to this protocol to define a custom attribute that can be stored in [`Logger.MetadataValueAttributes`](../metadatavalueattributes.md). Each conforming type acts as both the key (identified by its metatype) and the value.

This protocol is designed for **small, fixed-vocabulary attributes**. Each attribute value is stored as an `Int64` raw value, so attributes occupy minimal space (one inline slot without heap allocation for the common single-attribute case).

## Examples

```swift
public enum Priority: Int64, Sendable, Logger.MetadataValueAttributes.Attribute {
    case low = 1
    case high = 2
}
```

```swift
public struct Priority: Sendable, Hashable, Logger.MetadataValueAttributes.Attribute {
    public let rawValue: Int64
    public init(rawValue: Int64) {
        self.rawValue = rawValue
    }
    public static let low = Priority(rawValue: 1)
    public static let high = Priority(rawValue: 2)
}
```

## Relationships

### Inherits From
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadatavalueattributes/attribute)*