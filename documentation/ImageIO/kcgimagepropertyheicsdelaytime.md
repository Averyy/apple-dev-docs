# kCGImagePropertyHEICSDelayTime

**Framework**: Image I/O  
**Kind**: var

The number of seconds to wait before displaying the next image in the sequence, clamped to a minimum of `0.1` seconds.

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
let kCGImagePropertyHEICSDelayTime: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) with a floating-point value. The value of this key is never less than 100 millseconds, and the system adjusts values less than that amount to 100 milliseconds, as needed. See [`kCGImagePropertyHEICSUnclampedDelayTime`](kcgimagepropertyheicsunclampeddelaytime.md).

## See Also

- [let kCGImagePropertyHEICSFrameInfoArray: CFString](kcgimagepropertyheicsframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyHEICSUnclampedDelayTime: CFString](kcgimagepropertyheicsunclampeddelaytime.md)
  The unclamped number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyHEICSLoopCount: CFString](kcgimagepropertyheicsloopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyheicsdelaytime)*