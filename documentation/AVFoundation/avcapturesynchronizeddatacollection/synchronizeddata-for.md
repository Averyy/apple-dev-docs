# synchronizedData(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns synchronized data captured by the specified capture output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func synchronizedData(for captureOutput: AVCaptureOutput) -> AVCaptureSynchronizedData?
```

#### Return Value

A synchronized data object corresponding to the specified capture output.

## Parameters

- `captureOutput`: The capture output for which to retrieve data.

## See Also

- [var count: Int](avcapturesynchronizeddatacollection/count.md)
  The number of synchronized data objects in the collection.
- [subscript(AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/subscript(_:).md)
  Returns data captured by the specified capture output, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/synchronizeddata(for:))*