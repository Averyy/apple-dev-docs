# kCGImagePropertyHEICSUnclampedDelayTime

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

The unclamped number of seconds to wait before displaying the next image in the sequence.

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
let kCGImagePropertyHEICSUnclampedDelayTime: CFString
```

```c
extern CFStringRef const kCGImagePropertyHEICSUnclampedDelayTime;
```

## Discussion

The value of this key is a [`CFNumber`](../CoreFoundation/cfnumber.md) with a floating-point value.

## See Also

### Sequence Timing
- [let kCGImagePropertyHEICSFrameInfoArray: CFString](./kcgimagepropertyheicsframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyHEICSDelayTime: CFString](./kcgimagepropertyheicsdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence, clamped to a minimum of `0.1` seconds.
- [let kCGImagePropertyHEICSLoopCount: CFString](./kcgimagepropertyheicsloopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyheicsunclampeddelaytime)*