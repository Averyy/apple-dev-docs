---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(into:on:)"
framework: "swift-configuration/Configuration"
---

# chunked(into:on:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(into:on:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Subject, Collected>(into: Collected.Type, on projection: @escaping @Sendable (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, Collected> where Subject : Equatable, Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(into:on:))*