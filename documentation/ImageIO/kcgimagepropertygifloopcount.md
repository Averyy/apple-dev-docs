# kCGImagePropertyGIFLoopCount

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

The number of times to repeat an animated sequence.

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
let kCGImagePropertyGIFLoopCount: CFString
```

```c
extern CFStringRef const kCGImagePropertyGIFLoopCount;
```

## See Also

### Sequence Timing
- [let kCGImagePropertyGIFFrameInfoArray: CFString](./kcgimagepropertygifframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyGIFDelayTime: CFString](./kcgimagepropertygifdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence, clamped to a minimum of 100 milliseconds.
- [let kCGImagePropertyGIFUnclampedDelayTime: CFString](./kcgimagepropertygifunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertygifloopcount)*