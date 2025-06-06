# kCGImageAnimationStartIndex

**Framework**: Image I/O  
**Kind**: var

A property that specifies the index of the first frame of an animation.

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
let kCGImageAnimationStartIndex: CFString
```

#### Discussion

The value of this property is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) that contains an unsigned integer. To override the start index value in the image file, include this property in the options dictionary when animating an image.

## See Also

- [func CGAnimateImageAtURLWithBlock(CFURL, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimageaturlwithblock(_:_:_:).md)
  Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- [func CGAnimateImageDataWithBlock(CFData, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimagedatawithblock(_:_:_:).md)
  Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.
- [typealias CGImageSourceAnimationBlock](cgimagesourceanimationblock.md)
  The block to execute for each frame of an image animation.
- [let kCGImageAnimationDelayTime: CFString](kcgimageanimationdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImageAnimationLoopCount: CFString](kcgimageanimationloopcount.md)
  The number of times to repeat the animated sequence.
- [enum CGImageAnimationStatus](cgimageanimationstatus.md)
  Constants that indicate the result of animating an image sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimageanimationstartindex)*