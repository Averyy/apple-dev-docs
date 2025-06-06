# subscript(_:)

**Framework**: AVFoundation  
**Kind**: subscript

Returns data captured by the specified capture output, using subscript syntax.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
subscript(key: AVCaptureOutput) -> AVCaptureSynchronizedData? { get }
```

#### Return Value

A synchronized data object corresponding to the specified capture output.

#### Discussion

This call is equivalent to the [`synchronizedData(for:)`](avcapturesynchronizeddatacollection/synchronizeddata(for:).md) method, but allows subscript syntax.

## Parameters

- `key`: The capture output for which to retrieve data.

## See Also

- [var count: Int](avcapturesynchronizeddatacollection/count.md)
  The number of synchronized data objects in the collection.
- [func synchronizedData(for: AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/synchronizeddata(for:).md)
  Returns synchronized data captured by the specified capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/subscript(_:))*