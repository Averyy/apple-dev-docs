# contentView()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A view hierarchy that contains all the views which display the contents being searched.

**Availability**:
- macOS

## Declaration

```swift
optional func contentView() -> NSView?
```

```objc
- (NSView *) contentView;
```

## Return Value

The root view of the content view hierarchy.

## Discussion

This content view defines the view hierarchy to be dimmed during incremental search, if the `NSTextFinder` instance’s [`incrementalSearchingShouldDimContentView`](../nstextfinder/incrementalsearchingshoulddimcontentview.md) is [`true`](../../Swift/true.md). If this method is not implemented or returns `nil`, then the `NSTextFinder` instance will act as if [`incrementalSearchingShouldDimContentView`](../nstextfinder/incrementalsearchingshoulddimcontentview.md) is [`false`](../../Swift/false.md)

## See Also

### Find Bar View
- [var findBarView: NSView?](./findbarview.md)
  The view assigned by the text bar as the find bar view for the container.
- [var isFindBarVisible: Bool](./isfindbarvisible.md)
  Returns whether the container should display its find bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/contentview())*