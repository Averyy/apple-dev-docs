# CGImageSourceAnimationBlock

**Framework**: Image I/O  
**Kind**: typealias

The block to execute for each frame of an image animation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CGImageSourceAnimationBlock = (Int, CGImage, UnsafeMutablePointer<Bool>) -> Void
```

#### Discussion

During the animation of an image, the system calls this block for each successive frame of the animation. Use this block to display the new image in your app’s interface, and to update any additional details.

## Parameters

- `index`: The index of the image in the file.
- `image`: The image to display.
- `stop`: A Boolean flag set to   on input. To stop the animation, set the value of this parameter to  .

## See Also

- [func CGAnimateImageAtURLWithBlock(CFURL, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimageaturlwithblock(_:_:_:).md)
  Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- [func CGAnimateImageDataWithBlock(CFData, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimagedatawithblock(_:_:_:).md)
  Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.
- [let kCGImageAnimationStartIndex: CFString](kcgimageanimationstartindex.md)
  A property that specifies the index of the first frame of an animation.
- [let kCGImageAnimationDelayTime: CFString](kcgimageanimationdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImageAnimationLoopCount: CFString](kcgimageanimationloopcount.md)
  The number of times to repeat the animated sequence.
- [enum CGImageAnimationStatus](cgimageanimationstatus.md)
  Constants that indicate the result of animating an image sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourceanimationblock)*