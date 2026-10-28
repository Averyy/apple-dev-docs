# synchronizedData(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVCaptureSynchronizedData *) synchronizedDataForCaptureOutput:(AVCaptureOutput *) captureOutput;
```

## Return Value

A synchronized data object corresponding to the specified capture output.

## Parameters

- `captureOutput`: The capture output for which to retrieve data.

## See Also

### Accessing synchronized data
- [var count: Int](./count.md)
  The number of synchronized data objects in the collection.
- [subscript(AVCaptureOutput) -> AVCaptureSynchronizedData?](./subscript%28_%29.md)
  Returns data captured by the specified capture output, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/synchronizeddata(for:))*