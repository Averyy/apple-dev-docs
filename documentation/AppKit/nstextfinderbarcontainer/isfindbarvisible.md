# isFindBarVisible

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

Returns whether the container should display its find bar.

**Availability**:
- macOS ?+

## Declaration

```swift
var isFindBarVisible: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the [`findBarView`](nstextfinderbarcontainer/findbarview.md) property is set, then the find bar is displayed by the container. Otherwise, the find bar is not displayed.

The default value should be [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var findBarView: NSView?](nstextfinderbarcontainer/findbarview.md)
  The view assigned by the text bar as the find bar view for the container.
- [func contentView() -> NSView?](nstextfinderbarcontainer/contentview.md)
  A view hierarchy that contains all the views which display the contents being searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer/isfindbarvisible)*