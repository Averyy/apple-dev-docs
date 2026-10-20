# lengthOfBytes(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the number of bytes required to store the receiver in a given encoding.

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
func lengthOfBytes(using enc: UInt) -> Int
```

```objc
- (NSUInteger) lengthOfBytesUsingEncoding:(NSStringEncoding) enc;
```

#### Return Value

The number of bytes required to store the receiver in the encoding `enc` in a non-external representation. The length does not include space for a terminating `NULL` character. Returns `0` if the specified encoding cannot be used to convert the receiver or if the amount of memory required for storing the results of the encoding conversion would exceed [`NSIntegerMax`](../../ObjectiveC/nsintegermax.md).

#### Discussion

The result is exact and is returned in `O(n)` time.

## Parameters

- `enc`: The encoding for which to determine the receiver’s length.

## See Also

### Getting a String’s Length
- [var length: Int](./length.md)
  The number of UTF-16 code units in the receiver.
- [func maximumLengthOfBytes(using: UInt) -> Int](./maximumlengthofbytes%28using%29.md)
  Returns the maximum number of bytes needed to store the receiver in a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/lengthofbytes(using:))*