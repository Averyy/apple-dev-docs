# perform(_:performanceTime:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Initiates a specific pattern of haptic feedback to the user.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func perform(_ pattern: NSHapticFeedbackManager.FeedbackPattern, performanceTime: NSHapticFeedbackManager.PerformanceTime)
```

#### Discussion

In some cases, the system may override a call to this method. For example, a Force Touch trackpad won’t provide haptic feedback if the user isn’t touching the trackpad.

> ❗ **Important**:  Call this method only in response to user-initiated actions. Ideally, visual feedback, such as a highlight or appearance of an alignment guide, should accompany the feedback.

 Call this method only in response to user-initiated actions. Ideally, visual feedback, such as a highlight or appearance of an alignment guide, should accompany the feedback.

## Parameters

- `pattern`: A pattern of feedback to be provided to the user. For possible values, see  .
- `performanceTime`: The time when the feedback should be provided to the user. For possible values, see  .

## See Also

- [NSHapticFeedbackManager.PerformanceTime](nshapticfeedbackmanager/performancetime.md)
  A time at which to provide haptic feedback to the user.
- [class NSHapticFeedbackManager](nshapticfeedbackmanager.md)
  An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.
- [NSHapticFeedbackManager.FeedbackPattern](nshapticfeedbackmanager/feedbackpattern.md)
  A pattern of haptic feedback to be provided to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer/perform(_:performancetime:))*