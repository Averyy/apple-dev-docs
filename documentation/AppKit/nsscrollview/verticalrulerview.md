# verticalRulerView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s vertical ruler view.

**Availability**:
- macOS

## Declaration

```swift
var verticalRulerView: NSRulerView? { get set }
```

```objc
@property (strong, nullable) NSRulerView * verticalRulerView;
```

#### Discussion

The value of this property is `nil` when the scroll view has no vertical ruler view.

If the scroll view is set to display a vertical ruler view and doesn’t yet have one, this property creates an instance of the ruler view class set using the class method `setRulerViewClass(_:)`. You can use this property to override the default ruler class set using the class method `setRulerViewClass(_:)`.

Display of rulers is controlled using the [`rulersVisible`](./rulersvisible.md) property.

## See Also

### Managing Rulers
- [class var rulerViewClass: AnyClass!](./rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](./hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](./horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](./hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var rulersVisible: Bool](./rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticalrulerview)*