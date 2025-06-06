# CNScript.Frame

**Framework**: Cinematic  
**Kind**: struct

An object that represents what to focus on, and where to focus, in a given movie frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct Frame
```

## Topics

### Instance Properties
- [var allDetections: [CNDetection]](cnscript-1ispe/frame/alldetections.md)
  All detections for the Cinematic movie.
- [var focusDetection: CNDetection](cnscript-1ispe/frame/focusdetection.md)
  What to focus on in a given frame of the movie.
- [var focusDisparity: Float](cnscript-1ispe/frame/focusdisparity.md)
  Where to focus in a given frame of the movie.
- [var time: CMTime](cnscript-1ispe/frame/time.md)
  The time of the focus transition.
### Instance Methods
- [func bestDetection(for: CNDetectionGroupID) -> CNDetection?](cnscript-1ispe/frame/bestdetection(for:).md)
  The best detection to focus on in a frame among those within the given detection group.
- [func detection(for: CNDetectionID) -> CNDetection?](cnscript-1ispe/frame/detection(for:).md)
  The detection in the frame with the given detection ID, if any.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/frame)*