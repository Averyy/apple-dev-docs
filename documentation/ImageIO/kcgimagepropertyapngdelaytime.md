# kCGImagePropertyAPNGDelayTime

**Framework**: Image I/O  
**Kind**: var

The number of seconds to wait before displaying the next image in an animated sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyAPNGDelayTime: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) with a floating-point value. The value of this key is never less than 50 millseconds, and the system adjusts values less than that amount to 50 milliseconds, as needed. See [`kCGImagePropertyAPNGUnclampedDelayTime`](kcgimagepropertyapngunclampeddelaytime.md).

## See Also

- [let kCGImagePropertyAPNGFrameInfoArray: CFString](kcgimagepropertyapngframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyAPNGUnclampedDelayTime: CFString](kcgimagepropertyapngunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGLoopCount: CFString](kcgimagepropertyapngloopcount.md)
  The number of times that an animated PNG should play through its frames before stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngdelaytime)*