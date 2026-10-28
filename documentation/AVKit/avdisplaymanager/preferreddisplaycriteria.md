# preferredDisplayCriteria

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A hint for the TV to set the display mode to best match the currently playing content’s display criteria.

**Availability**:
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var preferredDisplayCriteria: AVDisplayCriteria? { get set }
```

```objc
@property (nonatomic, copy, nullable) AVDisplayCriteria * preferredDisplayCriteria;
```

## Discussion

The display manager uses the preferred display criteria only when user settings allow. Set this property to `nil` to allow the system to guide you to a display mode that’s suitable for a wide range of video and nonvideo content.

## See Also

### Matching a video’s native display mode
- [var isDisplayCriteriaMatchingEnabled: Bool](./isdisplaycriteriamatchingenabled.md)
  A Boolean value that indicates whether the user has enabled display critera matching.
- [var isDisplayModeSwitchInProgress: Bool](./isdisplaymodeswitchinprogress.md)
  A Boolean value that indicates whether a display mode switch is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager/preferreddisplaycriteria)*