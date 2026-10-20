# appleITTRight

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The right region for iTT format captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class var appleITTRight: AVCaptionRegion { get }
```

```objc
@property (class, readonly) AVCaptionRegion * appleITTRightRegion;
```

#### Discussion

This region occupies the right 15% of the display area, and it uses a TBRL layout where a line progresses from top to bottom and the block extends from right to left. Lines are right justified.

## See Also

### Accessing defined regions
- [class var appleITTTop: AVCaptionRegion](./appleitttop.md)
  The top region for iTT format captions.
- [class var appleITTBottom: AVCaptionRegion](./appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTLeft: AVCaptionRegion](./appleittleft.md)
  The left region for iTT format captions.
- [class var subRipTextBottom: AVCaptionRegion](./subriptextbottom.md)
  The bottom caption region for SubRip Text (SRT) format captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleittright)*