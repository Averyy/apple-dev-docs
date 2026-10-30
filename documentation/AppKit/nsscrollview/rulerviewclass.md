# rulerViewClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default class to be used for ruler objects in NSScrollViews.

**Availability**:
- macOS

## Declaration

```swift
class var rulerViewClass: AnyClass! { get set }
```

```objc
@property (class, null_resettable) Class rulerViewClass;
```

## Discussion

This class is normally NSRulerView.

## See Also

### Managing rulers
- [var hasHorizontalRuler: Bool](./hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](./horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](./hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](./verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](./rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/rulerviewclass)*