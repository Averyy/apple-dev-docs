---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(by:)-7z81j"
framework: "swift-configuration/Configuration"
---

# chunked(by:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(by:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Signal>(by signal: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Self.Element : Sendable, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(by:)-7z81j)*