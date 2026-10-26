---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(_:)"
framework: "swift-configuration/Configuration"
---

# reductions(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reductions(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reductions(_ transform: @escaping @Sendable (Self.Element, Self.Element) async -> Self.Element) -> AsyncInclusiveReductionsSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(_:))*