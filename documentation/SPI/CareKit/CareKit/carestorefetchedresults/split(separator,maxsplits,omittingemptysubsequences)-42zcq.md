---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/split(separator:maxsplits:omittingemptysubsequences:)-42zcq"
framework: "CareKit/CareKit"
---

# split(separator:maxSplits:omittingEmptySubsequences:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Collection.split(separator:maxSplits:omittingEmptySubsequences:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func split<C>(separator: C, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true) -> [Self.SubSequence] where C : Collection, Self.Element == C.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/split(separator:maxsplits:omittingemptysubsequences:)-42zcq)*