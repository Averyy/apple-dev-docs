---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:into:)-woc3"
framework: "swift-configuration/Configuration"
---

# chunks(ofCount:or:into:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:into:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunks<Signal, Collected>(ofCount count: Int, or signal: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:into:)-woc3)*