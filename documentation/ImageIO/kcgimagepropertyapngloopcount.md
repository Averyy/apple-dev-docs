# kCGImagePropertyAPNGLoopCount

**Framework**: Image I/O  
**Kind**: var

The number of times that an animated PNG should play through its frames before stopping.

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
let kCGImagePropertyAPNGLoopCount: CFString
```

#### Discussion

A value of `0` means the PNG repeats forever.

## See Also

- [let kCGImagePropertyAPNGFrameInfoArray: CFString](kcgimagepropertyapngframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyAPNGDelayTime: CFString](kcgimagepropertyapngdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGUnclampedDelayTime: CFString](kcgimagepropertyapngunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngloopcount)*