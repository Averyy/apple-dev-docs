# CGImageAnimationStatus

**Framework**: Image I/O  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the result of animating an image sequence.

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
enum CGImageAnimationStatus
```

```c
enum CGImageAnimationStatus : OSStatus;
```

## Topics

### Animation Status
- [CGImageAnimationStatus.allocationFailure](./cgimageanimationstatus/allocationfailure.md)
- [CGImageAnimationStatus.corruptInputImage](./cgimageanimationstatus/corruptinputimage.md)
- [CGImageAnimationStatus.incompleteInputImage](./cgimageanimationstatus/incompleteinputimage.md)
- [CGImageAnimationStatus.parameterError](./cgimageanimationstatus/parametererror.md)
- [CGImageAnimationStatus.unsupportedFormat](./cgimageanimationstatus/unsupportedformat.md)
### Initializers
- [init?(rawValue: OSStatus)](./cgimageanimationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [let kCGImageAnimationLoopCount: CFString](./kcgimageanimationloopcount.md)
  The number of times to repeat the animated sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimageanimationstatus)*