# compare(_:to:)

**Framework**: Foundation  
**Kind**: method

Returns a comparison result value that indicates the sort order of two objects.

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
func compare(_ object1: Any, to object2: Any) -> ComparisonResult
```

#### Return Value

[`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md) if `object1` is less than `object2`, [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md) if `object1` is greater than `object2`, or [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md) if `object1` is equal to `object2`.

#### Discussion

The ordering is determined by comparing the values specified by [`key`](nssortdescriptor/key.md) of `object1` and `object2` using the selector specified by [`selector`](nssortdescriptor/selector.md).

## Parameters

- `object1`: The object to compare with  . This object must have a property accessible using the key-path specified by  .
- `object2`: The object to compare with  . This object must have a property accessible using the key-path specified by  .

## See Also

- [var reversedSortDescriptor: Any](nssortdescriptor/reversedsortdescriptor.md)
  Returns a sort descriptor that reverses the sort order.
- [func allowEvaluation()](nssortdescriptor/allowevaluation.md)
  Forces a securely decoded sort descriptor to allow evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/compare(_:to:))*