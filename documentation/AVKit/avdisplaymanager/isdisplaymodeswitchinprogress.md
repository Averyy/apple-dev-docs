# isDisplayModeSwitchInProgress

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether a display mode switch is in progress.

**Availability**:
- tvOS 11.2+

## Declaration

```swift
var isDisplayModeSwitchInProgress: Bool { get }
```

#### Discussion

While this property value is [`true`](https://developer.apple.com/documentation/swift/true), your app should behave as if the display is currently changing modes, and may be temporarily blank. The accuracy of this property value depends on the TV hardware and the nature of the mode switch. When displaying temporary content or user interface elements, such as hints or tips, leave them visible for longer than the mode switch takes, to ensure the user sees them.

This property is key-value observable.

## See Also

- [var preferredDisplayCriteria: AVDisplayCriteria?](avdisplaymanager/preferreddisplaycriteria.md)
  A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [var isDisplayCriteriaMatchingEnabled: Bool](avdisplaymanager/isdisplaycriteriamatchingenabled.md)
  A Boolean value that indicates whether the user has enabled display critera matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager/isdisplaymodeswitchinprogress)*