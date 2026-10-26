---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reduce(_:_:)"
framework: "swift-configuration/Configuration"
---

# reduce(_:_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reduce(_:_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Self.Element) async throws -> Result) async rethrows -> Result
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/reduce(_:_:))*