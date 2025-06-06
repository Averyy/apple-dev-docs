# keyboardDismissPadding

**Framework**: UIKit  
**Kind**: property

A value that adds padding above the keyboard to increase the size of the touch area for the scrolling dismissal gesture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var keyboardDismissPadding: CGFloat { get set }
```

#### Discussion

Defaults to `0`. The system treats negative values as `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/keyboarddismisspadding)*