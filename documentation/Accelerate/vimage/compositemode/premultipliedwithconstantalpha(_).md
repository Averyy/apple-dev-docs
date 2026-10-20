# vImage.CompositeMode.premultipliedWithConstantAlpha(_:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Performs premultiplied alpha compositing of two images, using a single alpha value for the entire image.

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
case premultipliedWithConstantAlpha(ComponentType)
```

## See Also

### Enumeration Cases
- [vImage.CompositeMode.nonpremultiplied](./nonpremultiplied.md)
  Composite two non-premultiplied images, to produce a non-premultiplied result.
- [vImage.CompositeMode.nonpremultipliedToPremultiplied](./nonpremultipliedtopremultiplied.md)
  Blends a nonpremultiplied top image into a premultiplied bottom image and returns a premultiplied result.
- [vImage.CompositeMode.premultiplied](./premultiplied.md)
  Blends two premultiplied images to produce a premultiplied result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/compositemode/premultipliedwithconstantalpha(_:))*