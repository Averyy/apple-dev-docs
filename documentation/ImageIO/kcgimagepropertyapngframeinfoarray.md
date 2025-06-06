# kCGImagePropertyAPNGFrameInfoArray

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
let kCGImagePropertyAPNGFrameInfoArray: CFString
```

#### Discussion

The value of this property is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). Each [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) in the array contains timing information about an image in the sequence.

## See Also

- [let kCGImagePropertyAPNGDelayTime: CFString](kcgimagepropertyapngdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGUnclampedDelayTime: CFString](kcgimagepropertyapngunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGLoopCount: CFString](kcgimagepropertyapngloopcount.md)
  The number of times that an animated PNG should play through its frames before stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngframeinfoarray)*