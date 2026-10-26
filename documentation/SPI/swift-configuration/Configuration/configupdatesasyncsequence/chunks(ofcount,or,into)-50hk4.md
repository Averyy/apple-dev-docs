---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:into:)-50hk4"
framework: "swift-configuration/Configuration"
---

# chunks(ofCount:or:into:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:or:into:)`.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunks<C, Collected>(ofCount count: Int, or timer: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:or:into:)-50hk4)*