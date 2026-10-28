---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/snapshot()"
framework: "swift-configuration/Configuration"
---

# snapshot()

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns an immutable snapshot of the provider’s current state.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func snapshot() -> any ConfigSnapshot
```

Available when `Snapshot` conforms to `FileConfigSnapshot`.

## Return Value

An immutable snapshot that represents the current provider state.

## Discussion

Snapshots provide consistent access to multiple configuration values by capturing the provider’s state at a specific point in time. This prevents values from changing between reads, which is useful for reading related configuration keys together.

Snapshots are designed to be lightweight and can be created frequently without significant performance impact.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/snapshot())*