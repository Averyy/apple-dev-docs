# kCGImagePropertyWebPDelayTime

**Framework**: Image I/O  
**Kind**: var

The number of seconds to wait before displaying the next image in the sequence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let kCGImagePropertyWebPDelayTime: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) with a floating-point value. The value of this key is never less than 100 millseconds, and the system adjusts values less than that amount to 100 milliseconds, as needed. See [`kCGImagePropertyGIFUnclampedDelayTime`](kcgimagepropertygifunclampeddelaytime.md).

## See Also

- [let kCGImagePropertyWebPFrameInfoArray: CFString](kcgimagepropertywebpframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyWebPUnclampedDelayTime: CFString](kcgimagepropertywebpunclampeddelaytime.md)
  The unadjusted number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPLoopCount: CFString](kcgimagepropertywebploopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertywebpdelaytime)*