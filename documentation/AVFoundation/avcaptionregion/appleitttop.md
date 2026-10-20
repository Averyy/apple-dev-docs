# appleITTTop

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The top region for iTT format captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class var appleITTTop: AVCaptionRegion { get }
```

```objc
@property (class, readonly) AVCaptionRegion * appleITTTopRegion;
```

#### Discussion

This region is available when working with iTT captions. It occupies the top 15% of the display area, and it uses a LRTB layout where a line progresses from left to right and the block extends from top to bottom. Lines are top justified.

## See Also

### Accessing defined regions
- [class var appleITTBottom: AVCaptionRegion](./appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTLeft: AVCaptionRegion](./appleittleft.md)
  The left region for iTT format captions.
- [class var appleITTRight: AVCaptionRegion](./appleittright.md)
  The right region for iTT format captions.
- [class var subRipTextBottom: AVCaptionRegion](./subriptextbottom.md)
  The bottom caption region for SubRip Text (SRT) format captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleitttop)*