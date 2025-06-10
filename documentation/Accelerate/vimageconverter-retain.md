# vImageConverter_Retain

**Framework**: Accelerate  
**Kind**: func

Retains a vImage converter.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
void vImageConverter_Retain(vImageConverterRef converter);
```

#### Discussion

Retain a [`vImageConverter`](vimageconverter.md) instance when you receive it from elsewhere (that is, you didn’t create or copy it) and you want it to persist. If you retain a [`vImageConverter`](vimageconverter.md) instance you’re responsible for releasing it (see [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

## See Also

- [vImageConverter_Release](vimageconverter_release.md)
  Releases a vImage converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_retain)*