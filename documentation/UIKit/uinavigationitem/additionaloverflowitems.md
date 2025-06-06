# additionalOverflowItems

**Framework**: UIKit  
**Kind**: property

Additional items to present in the overflow menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var additionalOverflowItems: UIDeferredMenuElement? { get set }
```

#### Discussion

When you assign a non-`nil` value to this property, the overflow menu button appears on the trailing edge of the navigation bar. This button appears regardless of whether you provide menu elements in the callback for the [`UIDeferredMenuElement`](uideferredmenuelement.md).

The system presents any menu elements you return in the callback for [`UIDeferredMenuElement`](uideferredmenuelement.md) in the overflow menu. The system also populates the overflow menu with any items that can’t fit in the navigation bar due to layout space constraints.

## See Also

- [var overflowPresentationSource: (any UIPopoverPresentationControllerSourceItem)?](uinavigationitem/overflowpresentationsource.md)
  The item you can use as an anchor to present a custom UI from the overflow menu button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems)*