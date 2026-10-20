# relative(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the range of indices described by this range expression within the given collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func relative<C>(to collection: C) -> Range<Bound> where Bound == C.Index, C : Collection
```

Available when `Bound` conforms to `Comparable`.

#### Return Value

A range suitable for slicing `collection`. The returned range is *not* guaranteed to be inside the bounds of `collection`. Callers should apply the same preconditions to the return value as they would to a range provided directly by the user.

## Parameters

- `collection`: The collection to evaluate this range expression in relation to.

## See Also

### Converting Ranges
- [init?(NSRange, in: String)](./init%28_,in%29-5cclx.md)
- [init?<S>(NSRange, in: S)](./init%28_,in%29-5qfor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/relative(to:))*