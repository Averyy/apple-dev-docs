# vImage.EdgeMode.fill(backgroundColor:)

**Framework**: Accelerate  
**Kind**: case

An edge mode that uses the background color for missing pixels.

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
case fill(backgroundColor: PixelType)
```

## Parameters

- `backgroundColor`: The background color.

## See Also

- [vImage.EdgeMode.copyInPlace](vimage/edgemode/copyinplace.md)
  An edge mode that copies the value of the edge pixel in the source to the destination.
- [vImage.EdgeMode.extend](vimage/edgemode/extend.md)
  An edge mode that extends the edges of the image infinitely.
- [vImage.EdgeMode.truncateKernel](vimage/edgemode/truncatekernel.md)
  An edge mode that uses only the part of the kernel that overlaps the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/edgemode/fill(backgroundcolor:))*