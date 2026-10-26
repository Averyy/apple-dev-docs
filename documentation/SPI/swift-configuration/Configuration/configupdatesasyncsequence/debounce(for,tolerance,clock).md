---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/debounce(for:tolerance:clock:)"
framework: "swift-configuration/Configuration"
---

# debounce(for:tolerance:clock:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.debounce(for:tolerance:clock:)`.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func debounce<C>(for interval: C.Instant.Duration, tolerance: C.Instant.Duration? = nil, clock: C) -> AsyncDebounceSequence<Self, C> where Self : Sendable, C : Clock, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/debounce(for:tolerance:clock:))*