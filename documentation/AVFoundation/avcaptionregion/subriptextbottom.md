# subRipTextBottom

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The bottom caption region for SubRip Text (SRT) format captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class var subRipTextBottom: AVCaptionRegion { get }
```

```objc
@property (class, readonly) AVCaptionRegion * subRipTextBottomRegion;
```

#### Discussion

This region is suitable for SRT format, and it occupies the entire video display area. The region uses a [`AVCaptionRegion.WritingMode.leftToRightAndTopToBottom`](./writingmode-swift.enum/lefttorightandtoptobottom.md) writing mode, where a line progresses left to right and the block extends from top to bottom. The system stacks each line of text with bottom justification.

## See Also

### Accessing defined regions
- [class var appleITTTop: AVCaptionRegion](./appleitttop.md)
  The top region for iTT format captions.
- [class var appleITTBottom: AVCaptionRegion](./appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTLeft: AVCaptionRegion](./appleittleft.md)
  The left region for iTT format captions.
- [class var appleITTRight: AVCaptionRegion](./appleittright.md)
  The right region for iTT format captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/subriptextbottom)*