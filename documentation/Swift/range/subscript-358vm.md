# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the subsequence bounded by the given range.

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
subscript(bounds: Range<Range<Bound>.Index>) -> Range<Bound> { get }
```

## Parameters

- `bounds`: A range of the range’s indices. The upper and lower   bounds of the   range must be valid indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/subscript(_:)-358vm)*