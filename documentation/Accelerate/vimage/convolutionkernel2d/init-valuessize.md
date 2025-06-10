# init(values:size:)

**Framework**: Accelerate  
**Kind**: init

Returns a new convolution kernel structure with the size you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(values: [ComponentType], size: vImage.Size)
```

## Parameters

- `values`: The kernel weights or structuring element values that must contain   elements.
- `size`: The size of the kernel. The width and height of the kernel that must be a positive, odd numbers.

## See Also

- [init(values: [ComponentType], width: Int, height: Int)](vimage/convolutionkernel2d/init(values:width:height:).md)
  Returns a new convolution kernel structure with the width and height you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/convolutionkernel2d/init(values:size:))*