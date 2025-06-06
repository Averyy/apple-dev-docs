# delegate

**Framework**: UIKit  
**Kind**: property

An object that can fine-tune the large content viewer interactions, especially in the presence of other gesture recognizers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UILargeContentViewerInteractionDelegate)? { get }
```

## See Also

- [var gestureRecognizerForExclusionRelationship: UIGestureRecognizer](uilargecontentviewerinteraction/gesturerecognizerforexclusionrelationship.md)
  A gesture recognizer that you can use to set up simultaneous recognition or failure relationships with other gesture recognizers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/delegate)*