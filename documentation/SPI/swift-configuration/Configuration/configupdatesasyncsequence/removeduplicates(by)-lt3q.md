---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/removeduplicates(by:)-lt3q"
framework: "swift-configuration/Configuration"
---

# removeDuplicates(by:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.removeDuplicates(by:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func removeDuplicates(by predicate: @escaping @Sendable (Self.Element, Self.Element) async -> Bool) -> AsyncRemoveDuplicatesSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/removeduplicates(by:)-lt3q)*