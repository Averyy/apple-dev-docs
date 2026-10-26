---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:into:)"
framework: "swift-configuration/Configuration"
---

# chunks(ofCount:into:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunks(ofCount:into:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunks<Collected>(ofCount count: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunks(ofcount:into:))*