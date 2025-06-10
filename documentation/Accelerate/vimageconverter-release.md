# vImageConverter_Release

**Framework**: Accelerate  
**Kind**: func

Releases a vImage converter.

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
void vImageConverter_Release(vImageConverterRef converter);
```

#### Discussion

If you create or explicitly retain (see [`vImageConverter_Retain`](vimageconverter_retain.md)) a [`vImageConverter`](vimageconverter.md) instance, you’re responsible for releasing it when you no longer need it (see [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

## See Also

- [vImageConverter_Retain](vimageconverter_retain.md)
  Retains a vImage converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_release)*