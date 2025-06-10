# maximumLengthOfBytes(using:)

**Framework**: Foundation  
**Kind**: method

Returns the maximum number of bytes needed to store the receiver in a given encoding.

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
func maximumLengthOfBytes(using enc: UInt) -> Int
```

#### Return Value

The maximum number of bytes needed to store the receiver in `encoding` in a non-external representation. The length does not include space for a terminating `NULL` character. Returns `0` if the amount of memory required for storing the results of the encoding conversion would exceed [`NSIntegerMax`](https://developer.apple.com/documentation/ObjectiveC/NSIntegerMax).

#### Discussion

The result is an estimate and is returned in `O(1)` time; the estimate may be considerably greater than the actual length needed.

## Parameters

- `enc`: The encoding for which to determine the receiver’s length.

## See Also

- [var length: Int](nsstring/length.md)
  The number of UTF-16 code units in the receiver.
- [func lengthOfBytes(using: UInt) -> Int](nsstring/lengthofbytes(using:).md)
  Returns the number of bytes required to store the receiver in a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/maximumlengthofbytes(using:))*