# appleITTLeft

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The left region for iTT format captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class var appleITTLeft: AVCaptionRegion { get }
```

```objc
@property (class, readonly) AVCaptionRegion * appleITTLeftRegion;
```

#### Discussion

This region occupies the left 15% of the display area, and it uses a TBRL layout where a line progresses from top to bottom and the block extends from right to left. Lines are left justified.

## See Also

### Accessing defined regions
- [class var appleITTTop: AVCaptionRegion](./appleitttop.md)
  The top region for iTT format captions.
- [class var appleITTBottom: AVCaptionRegion](./appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTRight: AVCaptionRegion](./appleittright.md)
  The right region for iTT format captions.
- [class var subRipTextBottom: AVCaptionRegion](./subriptextbottom.md)
  The bottom caption region for SubRip Text (SRT) format captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleittleft)*