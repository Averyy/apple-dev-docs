# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized mutable data object capable of holding the specified number of bytes.

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
init?(capacity: Int)
```

#### Return Value

An initialized `NSMutableData` object capable of holding `capacity` bytes. The returned object has the same memory alignment guarantees as `malloc(_:)`.

#### Discussion

This method doesn’t necessarily allocate the requested memory right away. Mutable data objects allocate additional memory as needed, so `capacity` simply establishes the object’s initial capacity. When it does allocate the initial memory, though, it allocates the specified amount. This method sets the length of the data object to `0`.

If the capacity specified in `capacity` is greater than four memory pages in size, this method may round the amount of requested memory up to the nearest full page.

## Parameters

- `capacity`: The number of bytes the data object can initially contain.

## See Also

- [init?(length: Int)](nsmutabledata/init(length:).md)
  Initializes and returns a mutable data object containing a given number of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/init(capacity:))*