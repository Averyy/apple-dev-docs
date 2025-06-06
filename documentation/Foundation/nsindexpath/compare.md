# compare(_:)

**Framework**: Foundation  
**Kind**: method

Indicates the depth-first traversal order of the receiving index path and another index path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func compare(_ otherObject: IndexPath) -> ComparisonResult
```

#### Return Value

The depth-first traversal ordering of the receiving index path and `indexPath`.

#### Discussion

- [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md): The receiving index path comes before `indexPath`.
- [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md): The receiving index path comes after `indexPath`.
- [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md): The receiving index path and `indexPath` are the same index path.

## Parameters

- `otherObject`: This value must not be  . If the value is  , the behavior is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/compare(_:))*