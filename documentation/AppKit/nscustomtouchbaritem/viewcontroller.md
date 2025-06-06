# viewController

**Framework**: AppKit  
**Kind**: property

A view controller whose view is displayed in the bar to represent this item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var viewController: NSViewController? { get set }
```

#### Discussion

When set, the item’s [`view`](nscustomtouchbaritem/view.md) property returns the view controller’s [`view`](nsviewcontroller/view.md) property.

The property is automatically set to `nil` if you provide your own value for the [`view`](nscustomtouchbaritem/view.md) property.

## See Also

- [var view: NSView](nscustomtouchbaritem/view.md)
  The view displayed in the bar to represent this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomtouchbaritem/viewcontroller)*