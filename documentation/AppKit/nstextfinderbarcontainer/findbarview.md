# findBarView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The view assigned by the text bar as the find bar view for the container.

**Availability**:
- macOS

## Declaration

```swift
var findBarView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * findBarView;
```

## Discussion

This property is managed by `NSTextFinder` and you must not set this property.

The container may freely modify the view’s width, but should not modify its height.

## See Also

### Find Bar View
- [func contentView() -> NSView?](./contentview%28%29.md)
  A view hierarchy that contains all the views which display the contents being searched.
- [var isFindBarVisible: Bool](./isfindbarvisible.md)
  Returns whether the container should display its find bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/findbarview)*