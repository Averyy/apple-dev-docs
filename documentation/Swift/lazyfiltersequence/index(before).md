# index(before:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the position immediately before the given index.

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
func index(before i: LazyFilterSequence<Base>.Index) -> LazyFilterSequence<Base>.Index
```

Available when `Base` conforms to `BidirectionalCollection`.

## Return Value

The index value immediately before `i`.

## Parameters

- `i`: A valid index of the collection. `i` must be greater than `startIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/index(before:))*