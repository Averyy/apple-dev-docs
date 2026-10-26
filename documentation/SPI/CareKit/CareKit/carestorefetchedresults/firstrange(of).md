---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/firstrange(of:)"
framework: "CareKit/CareKit"
---

# firstRange(of:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Collection.firstRange(of:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func firstRange<C>(of other: C) -> Range<Self.Index>? where C : Collection, Self.Element == C.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/firstrange(of:))*