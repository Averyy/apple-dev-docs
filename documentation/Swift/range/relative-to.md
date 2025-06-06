# relative(to:)

**Framework**: Swift  
**Kind**: method

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

#### Return Value

A range suitable for slicing `collection`. The returned range is  guaranteed to be inside the bounds of `collection`. Callers should apply the same preconditions to the return value as they would to a range provided directly by the user.

## Parameters

- `collection`: The collection to evaluate this range expression   in relation to.

## See Also

- [init?(NSRange, in: String)](range/init(_:in:)-5cclx.md)
- [init?<S>(NSRange, in: S)](range/init(_:in:)-5qfor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/relative(to:))*