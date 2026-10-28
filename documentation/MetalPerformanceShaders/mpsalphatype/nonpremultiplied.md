# MPSAlphaType.nonPremultiplied

**Framework**: Metal Performance Shaders  
**Kind**: case  
**Role**: Case

The image is not premultiplied by alpha.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case nonPremultiplied
```

```c
MPSAlphaTypeNonPremultiplied
```

## Discussion

The image uses non-premultiplied alpha. Alpha is not guaranteed to be 1.

## See Also

### Constants
- [MPSAlphaType.alphaIsOne](./alphaisone.md)
  Alpha is guaranteed to be 1.
- [MPSAlphaType.premultiplied](./premultiplied.md)
  The image is premultiplied by alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype/nonpremultiplied)*