# compare(byRank:)

**Framework**: Core Spotlight  
**Kind**: method

Compares two items by rank and returns the result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func compare(byRank other: CSSearchableItem) -> ComparisonResult
```

#### Return Value

A comparison result that indicates the ranked order of the items.

#### Discussion

Call this function when you want to compare the current item with the one you specify. The method compares the ranks of the items.

## Parameters

- `other`: The other item to compare against the current one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/compare(byrank:))*