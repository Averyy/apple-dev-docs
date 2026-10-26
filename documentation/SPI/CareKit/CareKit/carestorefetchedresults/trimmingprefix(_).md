---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/trimmingprefix(_:)"
framework: "CareKit/CareKit"
---

# trimmingPrefix(_:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Collection.trimmingPrefix(_:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func trimmingPrefix<Prefix>(_ prefix: Prefix) -> Self.SubSequence where Prefix : Sequence, Self.Element == Prefix.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/trimmingprefix(_:))*