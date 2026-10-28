# isFindBarVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns whether the container should display its find bar.

**Availability**:
- macOS

## Declaration

```swift
var isFindBarVisible: Bool { get set }
```

```objc
@property (getter=isFindBarVisible) BOOL findBarVisible;
```

## Discussion

When this property is [`true`](../../Swift/true.md) and the [`findBarView`](./findbarview.md) property is set, then the find bar is displayed by the container. Otherwise, the find bar is not displayed.

The default value should be [`false`](../../Swift/false.md).

## See Also

### Find Bar View
- [var findBarView: NSView?](./findbarview.md)
  The view assigned by the text bar as the find bar view for the container.
- [func contentView() -> NSView?](./contentview%28%29.md)
  A view hierarchy that contains all the views which display the contents being searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/isfindbarvisible)*