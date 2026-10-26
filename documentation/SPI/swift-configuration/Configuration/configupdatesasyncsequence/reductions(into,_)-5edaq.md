---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(into:_:)-5edaq"
framework: "swift-configuration/Configuration"
---

# reductions(into:_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reductions(into:_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reductions<Result>(into initial: Result, _ transform: @escaping @Sendable (inout Result, Self.Element) async -> Void) -> AsyncExclusiveReductionsSequence<Self, Result>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reductions(into:_:)-5edaq)*