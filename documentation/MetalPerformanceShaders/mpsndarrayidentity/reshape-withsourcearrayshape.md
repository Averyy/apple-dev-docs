# reshape(withSourceArray:shape:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reshape(withSourceArray sourceArray: MPSNDArray, shape: [NSNumber]) -> MPSNDArray?
```

#### Return Value

A new array view of `sourceArray` is returned. Or `nil` If aliasing is not possible.

#### Discussion

Do a reshape operation on the CPU.

## Parameters

- `sourceArray`: The source NDArray.
- `shape`: The new shape in Tensorflow dimension order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity/reshape(withsourcearray:shape:))*