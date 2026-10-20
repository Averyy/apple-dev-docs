# kCGImagePropertyHEICSFrameInfoArray

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

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
let kCGImagePropertyHEICSFrameInfoArray: CFString
```

```c
extern CFStringRef const kCGImagePropertyHEICSFrameInfoArray;
```

#### Discussion

The value of this property is a [`CFArray`](../CoreFoundation/cfarray.md). Each [`CFDictionary`](../CoreFoundation/cfdictionary.md) in the array contains timing information about an image in the sequence.

## See Also

### Sequence Timing
- [let kCGImagePropertyHEICSDelayTime: CFString](./kcgimagepropertyheicsdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence, clamped to a minimum of `0.1` seconds.
- [let kCGImagePropertyHEICSUnclampedDelayTime: CFString](./kcgimagepropertyheicsunclampeddelaytime.md)
  The unclamped number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyHEICSLoopCount: CFString](./kcgimagepropertyheicsloopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyheicsframeinfoarray)*