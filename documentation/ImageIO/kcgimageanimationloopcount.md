# kCGImageAnimationLoopCount

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

The number of times to repeat the animated sequence.

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
let kCGImageAnimationLoopCount: CFString
```

```c
extern CFStringRef const kCGImageAnimationLoopCount;
```

## Discussion

The value of this property is a [`CFNumber`](../CoreFoundation/cfnumber.md) that contains an unsigned integer. To override the loop count value in the image file, include this property in the options dictionary when animating an image.

You may specify [`kCFNumberPositiveInfinity`](../CoreFoundation/kcfnumberpositiveinfinity.md) for this property to animate the images continuously.

## See Also

### Animations
- [func CGAnimateImageAtURLWithBlock(CFURL, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](./cganimateimageaturlwithblock%28_,_,_%29.md)
  Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- [func CGAnimateImageDataWithBlock(CFData, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](./cganimateimagedatawithblock%28_,_,_%29.md)
  Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.
- [typealias CGImageSourceAnimationBlock](./cgimagesourceanimationblock.md)
  The block to execute for each frame of an image animation.
- [let kCGImageAnimationStartIndex: CFString](./kcgimageanimationstartindex.md)
  A property that specifies the index of the first frame of an animation.
- [let kCGImageAnimationDelayTime: CFString](./kcgimageanimationdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [enum CGImageAnimationStatus](./cgimageanimationstatus.md)
  Constants that indicate the result of animating an image sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimageanimationloopcount)*