# makeArray(of:channelCount:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns an array of `width * height * channelCount` values that’s a copy of the buffer’s visible contents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func makeArray<U>(of scalarType: U.Type, channelCount: Int) -> [U]
```

Available when `Format` is `vImage.DynamicPixelFormat`.

#### Return Value

An array of `scalarType` values that  contains the source buffer’s contents.

## Parameters

- `scalarType`: The scalar type of each array element.
- `channelCount`: The number of channels in the pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/makearray(of:channelcount:))*