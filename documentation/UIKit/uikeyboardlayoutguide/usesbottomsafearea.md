# usesBottomSafeArea

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the layout guide uses the view’s safe area layout guide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var usesBottomSafeArea: Bool { get set }
```

#### Discussion

Defaults to [`true`](https://developer.apple.com/documentation/swift/true), indicating that the layout guide ties to the [`bottomAnchor`](uilayoutguide/bottomanchor.md) of the view’s [`safeAreaLayoutGuide`](uiview/safearealayoutguide.md).

Set to [`false`](https://developer.apple.com/documentation/swift/false) to tie the layout guide to the [`bottomAnchor`](uiview/bottomanchor.md) of the view instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/usesbottomsafearea)*