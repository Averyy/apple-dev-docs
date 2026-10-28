# kCGImagePropertyWebPFrameInfoArray

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kCGImagePropertyWebPFrameInfoArray;
```

## Discussion

The value of this property is a [`CFArray`](../CoreFoundation/cfarray.md). Each [`CFDictionary`](../CoreFoundation/cfdictionary.md) in the array contains timing information about an image in the sequence.

## See Also

### Sequence Timing
- [let kCGImagePropertyWebPDelayTime: CFString](./kcgimagepropertywebpdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPUnclampedDelayTime: CFString](./kcgimagepropertywebpunclampeddelaytime.md)
  The unadjusted number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyWebPLoopCount: CFString](./kcgimagepropertywebploopcount.md)
  The number of times to play the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertywebpframeinfoarray)*