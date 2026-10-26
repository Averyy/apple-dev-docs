---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(_:_:)-4n4af"
framework: "swift-configuration/Configuration"
---

# reductions(_:_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reductions(_:_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reductions<Result>(_ initial: Result, _ transform: @escaping @Sendable (Result, Self.Element) async -> Result) -> AsyncExclusiveReductionsSequence<Self, Result>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(_:_:)-4n4af)*