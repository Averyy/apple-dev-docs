# isDisplayCriteriaMatchingEnabled

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user has enabled display critera matching.

**Availability**:
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var isDisplayCriteriaMatchingEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDisplayCriteriaMatchingEnabled) BOOL displayCriteriaMatchingEnabled;
```

#### Discussion

This value reflects the user’s current Match Content settings, which they set in the Settings app under Video and Audio > Match Content.

## See Also

### Matching a video’s native display mode
- [var preferredDisplayCriteria: AVDisplayCriteria?](./preferreddisplaycriteria.md)
  A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [var isDisplayModeSwitchInProgress: Bool](./isdisplaymodeswitchinprogress.md)
  A Boolean value that indicates whether a display mode switch is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager/isdisplaycriteriamatchingenabled)*