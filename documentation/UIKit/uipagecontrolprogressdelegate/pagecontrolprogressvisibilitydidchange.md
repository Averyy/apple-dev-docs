# pageControlProgressVisibilityDidChange(_:)

**Framework**: UIKit  
**Kind**: method

Called when the page control progress visibility has changed, which could occur when the page control is being interacted with. The page control progress becomes hidden when the user begins to interact with the page control (when it begins continuous interaction), and is visible again when the user stops interacting with the control. Observe the page control progress visibility to pause or resume the paging content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func pageControlProgressVisibilityDidChange(_ progress: UIPageControlProgress)
```

#### Discussion

Example:

- (void)pageControlProgressVisibilityDidChange:(UIPageControlProgress *)progress { BOOL isProgressVisible = progress.isProgressVisible; if (isProgressVisible) { [self _resumeContentFromInteractionChanges]; } else { [self _pauseContentFromInteractionChanges]; } }


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange(_:))*