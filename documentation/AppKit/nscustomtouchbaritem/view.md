# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view displayed in the bar to represent this item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var view: NSView { get set }
```

```objc
@property (strong, readwrite) NSView * view;
```

## Discussion

By default, this property returns the value of [`view`](../nsviewcontroller/view.md) property from the view controller assigned to the [`viewController`](./viewcontroller.md) property.

If you set the value of this property, then the [`viewController`](./viewcontroller.md) property is automatically set to `nil`.

## See Also

### Providing item content
- [var viewController: NSViewController?](./viewcontroller.md)
  A view controller whose view is displayed in the bar to represent this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomtouchbaritem/view)*