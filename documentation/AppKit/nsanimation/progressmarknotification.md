# progressMarkNotification

**Framework**: AppKit  
**Kind**: property

Posted when the current progress of a running animation reaches one of its progress marks.

**Availability**:
- macOS ?+

## Declaration

```swift
class let progressMarkNotification: NSNotification.Name
```

#### Discussion

The notification object is a running `NSAnimation` object. The `userInfo` dictionary contains the current progress mark, accessed via the key `NSAnimationProgressMark`.

## See Also

- [func animation(NSAnimation, didReachProgressMark: NSAnimation.Progress)](nsanimationdelegate/animation(_:didreachprogressmark:).md)
  Sent to the delegate when an animation reaches a specific progress mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/progressmarknotification)*