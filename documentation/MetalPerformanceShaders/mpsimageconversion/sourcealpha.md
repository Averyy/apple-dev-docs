# sourceAlpha

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

Premultiplication description for the source texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var sourceAlpha: MPSAlphaType { get }
```

```objc
@property (nonatomic, readonly) MPSAlphaType sourceAlpha;
```

## Discussion

Most color space conversion operations can not work directly on premultiplied data. Use this property to tag premultiplied data so that the source texture can be un-premultiplied prior to the application of these transforms. The default value is [`MPSAlphaType.alphaIsOne`](../mpsalphatype/alphaisone.md).

## See Also

### Properties
- [var destinationAlpha: MPSAlphaType](./destinationalpha.md)
  Premultiplication description for the destination texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion/sourcealpha)*