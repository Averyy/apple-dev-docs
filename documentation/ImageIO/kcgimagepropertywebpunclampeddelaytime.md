# kCGImagePropertyWebPUnclampedDelayTime

**Framework**: Image I/O  
**Kind**: var

The unadjusted number of seconds to wait before displaying the next image in the sequence.

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
let kCGImagePropertyWebPUnclampedDelayTime: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) with a floating-point value.

## See Also

- [let kCGImagePropertyWebPFrameInfoArray: CFString](kcgimagepropertywebpframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyWebPDelayTime: CFString](kcgimagepropertywebpdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPLoopCount: CFString](kcgimagepropertywebploopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertywebpunclampeddelaytime)*