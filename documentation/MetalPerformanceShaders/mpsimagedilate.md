# MPSImageDilate

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that finds the maximum pixel value in a rectangular region by applying a dilation function.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageDilate
```

#### Overview

An [`MPSImageDilate`](mpsimagedilate.md) filter behaves like the [`MPSImageAreaMax`](mpsimageareamax.md) filter, except Metal calculates the intensity at each position relative to a different value before determining which is the maximum pixel value, allowing for shaped, nonrectangular morphological probes.

The code example below shows pseudocode for the calculation that returns each pixel value:

```other
for each pixel in the filter window
    value = pixel[filterY][filterX] - filter[filterY*filter_width+filterX]
    if( value > bestValue ){
        result = value
        bestValue = value
    }
```

A filter that contains all zeros is identical to an [`MPSImageAreaMax`](mpsimageareamax.md) filter. Metal handles the center filter element as `0` to avoid causing a general darkening of the image, and it handles the [`edgeMode`](mpsunaryimagekernel/edgemode.md) property  as [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) for this filter.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagedilate/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, values: UnsafePointer<Float>)](mpsimagedilate/init(device:kernelwidth:kernelheight:values:).md)
  Initializes the kernel with a specified width, height, and weight values.
### Properties
- [var kernelHeight: Int](mpsimagedilate/kernelheight.md)
  The height of the filter window. which must be an odd number.
- [var kernelWidth: Int](mpsimagedilate/kernelwidth.md)
  The width of the filter window which must be an odd number.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Inherited By
- [MPSImageErode](mpsimageerode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSImageAreaMax](mpsimageareamax.md)
  A filter that finds the maximum pixel value in a rectangular region centered around each pixel in the source image.
- [class MPSImageAreaMin](mpsimageareamin.md)
  A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image.
- [class MPSImageErode](mpsimageerode.md)
  A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate)*