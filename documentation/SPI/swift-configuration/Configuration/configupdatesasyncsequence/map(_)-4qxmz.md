---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/map(_:)-4qxmz"
framework: "swift-configuration/Configuration"
---

# map(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.map(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func map<Transformed>(_ transform: @escaping @Sendable (Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/map(_:)-4qxmz)*