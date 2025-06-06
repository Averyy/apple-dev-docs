# resetBytes(in:)

**Framework**: Foundation  
**Kind**: method

Sets a region of the data buffer to `0`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func resetBytes(in range: Range<Data.Index>)
```

#### Discussion

If `range` exceeds the bounds of the data, then the data is resized to fit.

## Parameters

- `range`: The range in the data to set to  .

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/resetbytes(in:))*