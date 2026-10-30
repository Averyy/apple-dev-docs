# horizontalRulerView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s horizontal ruler view.

**Availability**:
- macOS

## Declaration

```swift
var horizontalRulerView: NSRulerView? { get set }
```

```objc
@property (strong, nullable) NSRulerView * horizontalRulerView;
```

## Discussion

The value of this property is `nil` when the scroll view has no horizontal ruler view.

If the scroll view is set to display a horizontal ruler view and doesn’t yet have one, this property creates an instance of the ruler view class set using the class method `setRulerViewClass(_:)`. You can use this property to override the default ruler class set using the class method `setRulerViewClass(_:)`.

Display of rulers is controlled using the [`rulersVisible`](./rulersvisible.md) property.

## See Also

### Managing rulers
- [class var rulerViewClass: AnyClass!](./rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](./hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var hasVerticalRuler: Bool](./hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](./verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](./rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/horizontalrulerview)*