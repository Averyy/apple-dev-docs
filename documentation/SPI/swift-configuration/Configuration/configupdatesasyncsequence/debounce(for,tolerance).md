---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/debounce(for:tolerance:)"
framework: "swift-configuration/Configuration"
---

# debounce(for:tolerance:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.debounce(for:tolerance:)`.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func debounce(for interval: Duration, tolerance: Duration? = nil) -> AsyncDebounceSequence<Self, ContinuousClock> where Self : Sendable, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/debounce(for:tolerance:))*