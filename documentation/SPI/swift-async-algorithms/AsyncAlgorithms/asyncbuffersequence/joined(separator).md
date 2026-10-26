---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequence/joined(separator:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# joined(separator:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Concatenate an `AsyncSequence` of `AsyncSequence` elements with a separator.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func joined<Separator>(separator: Separator) -> AsyncJoinedBySeparatorSequence<Self, Separator> where Separator : AsyncSequence, Separator.Element == Self.Element.Element
```

Available when `Element` conforms to `AsyncSequence`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequence/joined(separator:))*