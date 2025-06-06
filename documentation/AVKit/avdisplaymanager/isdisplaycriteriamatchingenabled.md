# isDisplayCriteriaMatchingEnabled

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the user has enabled display critera matching.

**Availability**:
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var isDisplayCriteriaMatchingEnabled: Bool { get }
```

#### Discussion

This value reflects the user’s current Match Content settings, which they set in the Settings app under Video and Audio > Match Content.

## See Also

- [var preferredDisplayCriteria: AVDisplayCriteria?](avdisplaymanager/preferreddisplaycriteria.md)
  A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [var isDisplayModeSwitchInProgress: Bool](avdisplaymanager/isdisplaymodeswitchinprogress.md)
  A Boolean value that indicates whether a display mode switch is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager/isdisplaycriteriamatchingenabled)*