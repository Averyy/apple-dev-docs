---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:)-9w0pm"
framework: "swift-configuration/Configuration"
---

# chunks(ofCount:or:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunks<Signal>(ofCount count: Int, or signal: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Self.Element : Sendable, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:)-9w0pm)*