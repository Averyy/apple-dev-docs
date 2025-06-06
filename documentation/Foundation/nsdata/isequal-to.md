# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether this data object is the same as another.

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
func isEqual(to other: Data) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the contents of `otherData` are equal to the contents of the receiver, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Two data objects are equal if they hold the same number of bytes, and if the bytes at the same position in the objects are the same.

## Parameters

- `other`: The data object with which to compare the receiver.

## See Also

- [var length: Int](nsdata/length.md)
  The number of bytes contained by the data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/isequal(to:))*