---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/contains(_:)-5gcld"
framework: "CareKit/CareKit"
---

# contains(_:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Collection.contains(_:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func contains<C>(_ other: C) -> Bool where C : Collection, Self.Element == C.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/contains(_:)-5gcld)*