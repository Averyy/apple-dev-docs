# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Creates an empty data buffer of a specified size.

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
init(capacity: Int)
```

#### Discussion

This initializer doesn’t necessarily allocate the requested memory right away. `Data` allocates additional memory as needed, so `capacity` simply establishes the initial capacity. When it does allocate the initial memory, though, it allocates the specified amount.

This method sets the `count` of the data to 0.

If the capacity specified in `capacity` is greater than four memory pages in size, this may round the amount of requested memory up to the nearest full page.

## Parameters

- `capacity`: The size of the data.

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.
- [func resetBytes(in: Range<Data.Index>)](data/resetbytes(in:).md)
  Sets a region of the data buffer to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(capacity:))*