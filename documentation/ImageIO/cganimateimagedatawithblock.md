# CGAnimateImageDataWithBlock(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.

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
func CGAnimateImageDataWithBlock(_ data: CFData, _ options: CFDictionary?, _ block: @escaping CGImageSourceAnimationBlock) -> OSStatus
```

#### Return Value

A status code indicating the success or failure of the animation.

#### Discussion

The function executes the provided `block` for each frame of the animation. By default, the function uses the timing information contained in the image’s metadata. This information includes the number of seconds between individual frames, and the number of times to loop the animation. For example, the function uses the [`kCGImagePropertyGIFDelayTime`](kcgimagepropertygifdelaytime.md) and [`kCGImagePropertyGIFLoopCount`](kcgimagepropertygifloopcount.md) tags from a GIF image’s metadata. To override the default timing information, provide the appropriate keys in the `options` dictionary.

## Parameters

- `data`: The image data to animate.
- `options`: Additional playback options. Include the   or   keys to override the timing information in the image file. Include the   key to specify the index of the first image in the animation.
- `block`: The animation block to execute for each image frame. The system executes this block on the main queue, and at the intervals indicated by the image’s delay time metadata. Use this block to display the provided image in your interface.

## See Also

- [func CGAnimateImageAtURLWithBlock(CFURL, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimageaturlwithblock(_:_:_:).md)
  Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- [typealias CGImageSourceAnimationBlock](cgimagesourceanimationblock.md)
  The block to execute for each frame of an image animation.
- [let kCGImageAnimationStartIndex: CFString](kcgimageanimationstartindex.md)
  A property that specifies the index of the first frame of an animation.
- [let kCGImageAnimationDelayTime: CFString](kcgimageanimationdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImageAnimationLoopCount: CFString](kcgimageanimationloopcount.md)
  The number of times to repeat the animated sequence.
- [enum CGImageAnimationStatus](cgimageanimationstatus.md)
  Constants that indicate the result of animating an image sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cganimateimagedatawithblock(_:_:_:))*