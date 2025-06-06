# overflowPresentationSource

**Framework**: UIKit  
**Kind**: property

The item you can use as an anchor to present a custom UI from the overflow menu button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var overflowPresentationSource: (any UIPopoverPresentationControllerSourceItem)? { get }
```

#### Discussion

If the overflow menu button for the navigation item is visible, this property returns a non-`nil` item that you can use as a presentation source — for example, to present a custom popover that anchors to the overflow menu button. Otherwise, this property returns `nil`.

## See Also

- [var additionalOverflowItems: UIDeferredMenuElement?](uinavigationitem/additionaloverflowitems.md)
  Additional items to present in the overflow menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/overflowpresentationsource)*