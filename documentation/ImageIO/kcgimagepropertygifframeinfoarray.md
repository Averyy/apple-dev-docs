# kCGImagePropertyGIFFrameInfoArray

**Framework**: Image I/O  
**Kind**: var

An array of dictionaries that contain timing information for the image sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCGImagePropertyGIFFrameInfoArray: CFString
```

#### Discussion

The value of this property is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). Each [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) in the array contains timing information about an image in the sequence.

## See Also

- [let kCGImagePropertyGIFDelayTime: CFString](kcgimagepropertygifdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence, clamped to a minimum of 100 milliseconds.
- [let kCGImagePropertyGIFUnclampedDelayTime: CFString](kcgimagepropertygifunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyGIFLoopCount: CFString](kcgimagepropertygifloopcount.md)
  The number of times to repeat an animated sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertygifframeinfoarray)*