# prefersFullSizePreview

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates that the drag item preview should be shown at its full, original size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var prefersFullSizePreview: Bool { get set }
```

#### Discussion

Set [`prefersFullSizePreview`](uidropproposal/prefersfullsizepreview.md) to [`true`](https://developer.apple.com/documentation/swift/true) to show the preview at its original size, not scaled down to a smaller size. For example, you might set this property to [`true`](https://developer.apple.com/documentation/swift/true) when the user moves items from a nearby view and scaling down the preview is distracting.

This property applies only to drag and drop activities performed within the same app.

## See Also

- [var isPrecise: Bool](uidropproposal/isprecise.md)
  A Boolean value that proposes that the drop interaction define the drop location precisely, such as at a specific point within existing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropproposal/prefersfullsizepreview)*