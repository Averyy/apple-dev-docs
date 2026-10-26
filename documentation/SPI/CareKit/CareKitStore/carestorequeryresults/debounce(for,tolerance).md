---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/debounce(for:tolerance:)"
framework: "CareKit/CareKitStore"
---

# debounce(for:tolerance:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.debounce(for:tolerance:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func debounce(for interval: Duration, tolerance: Duration? = nil) -> AsyncDebounceSequence<Self, ContinuousClock> where Self : Sendable, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults/debounce(for:tolerance:))*