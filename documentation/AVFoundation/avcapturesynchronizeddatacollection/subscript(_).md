# subscript(_:)

**Framework**: AVFoundation  
**Kind**: subscript  
**Role**: Instance Subscript

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

```objc
- (AVCaptureSynchronizedData *) objectForKeyedSubscript:(AVCaptureOutput *) key;
```

#### Return Value

A synchronized data object corresponding to the specified capture output.

#### Discussion

This call is equivalent to the [`synchronizedData(for:)`](./synchronizeddata%28for%29.md) method, but allows subscript syntax.

## Parameters

- `key`: The capture output for which to retrieve data.

## See Also

### Accessing synchronized data
- [var count: Int](./count.md)
  The number of synchronized data objects in the collection.
- [func synchronizedData(for: AVCaptureOutput) -> AVCaptureSynchronizedData?](./synchronizeddata%28for%29.md)
  Returns synchronized data captured by the specified capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/subscript(_:))*