# kCGImagePropertyGIFDelayTime

**Framework**: Image I/O  
**Kind**: var

The number of seconds to wait before displaying the next image in an animated sequence, clamped to a minimum of 100 milliseconds.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyGIFDelayTime: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) with a floating-point value. The value of this key is never less than 100 millseconds, and the system adjusts values less than that amount to 100 milliseconds, as needed. See [`kCGImagePropertyGIFUnclampedDelayTime`](kcgimagepropertygifunclampeddelaytime.md).

## See Also

- [let kCGImagePropertyGIFFrameInfoArray: CFString](kcgimagepropertygifframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyGIFUnclampedDelayTime: CFString](kcgimagepropertygifunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyGIFLoopCount: CFString](kcgimagepropertygifloopcount.md)
  The number of times to repeat an animated sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertygifdelaytime)*