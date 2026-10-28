# progressMarkNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the current progress of a running animation reaches one of its progress marks.

**Availability**:
- macOS

## Declaration

```swift
class let progressMarkNotification: NSNotification.Name
```

```c
extern NSNotificationName NSAnimationProgressMarkNotification;
```

## Discussion

The notification object is a running `NSAnimation` object. The `userInfo` dictionary contains the current progress mark, accessed via the key `NSAnimationProgressMark`.

## See Also

### Related Documentation
- [func animation(NSAnimation, didReachProgressMark: NSAnimation.Progress)](../nsanimationdelegate/animation%28_,didreachprogressmark%29.md)
  Sent to the delegate when an animation reaches a specific progress mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/progressmarknotification)*