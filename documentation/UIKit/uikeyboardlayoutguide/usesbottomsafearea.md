# usesBottomSafeArea

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layout guide uses the view’s safe area layout guide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var usesBottomSafeArea: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL usesBottomSafeArea;
```

#### Discussion

Defaults to [`true`](../../Swift/true.md), indicating that the layout guide ties to the [`bottomAnchor`](../uilayoutguide/bottomanchor.md) of the view’s [`safeAreaLayoutGuide`](../uiview/safearealayoutguide.md).

Set to [`false`](../../Swift/false.md) to tie the layout guide to the [`bottomAnchor`](../uiview/bottomanchor.md) of the view instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/usesbottomsafearea)*