# kCGImagePropertyWebPFrameInfoArray

**Framework**: Image I/O  
**Kind**: var

An array of dictionaries that contain timing information for the image sequence.

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
let kCGImagePropertyWebPFrameInfoArray: CFString
```

#### Discussion

The value of this property is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). Each [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) in the array contains timing information about an image in the sequence.

## See Also

- [let kCGImagePropertyWebPDelayTime: CFString](kcgimagepropertywebpdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPUnclampedDelayTime: CFString](kcgimagepropertywebpunclampeddelaytime.md)
  The unadjusted number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPLoopCount: CFString](kcgimagepropertywebploopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertywebpframeinfoarray)*