# viewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A view controller whose view is displayed in the bar to represent this item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var viewController: NSViewController? { get set }
```

```objc
@property (strong, readwrite, nullable) NSViewController * viewController;
```

#### Discussion

When set, the item’s [`view`](./view.md) property returns the view controller’s [`view`](../nsviewcontroller/view.md) property.

The property is automatically set to `nil` if you provide your own value for the [`view`](./view.md) property.

## See Also

### Providing item content
- [var view: NSView](./view.md)
  The view displayed in the bar to represent this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomtouchbaritem/viewcontroller)*