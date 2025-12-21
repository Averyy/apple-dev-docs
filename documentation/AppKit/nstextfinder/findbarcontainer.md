# findBarContainer

**Framework**: AppKit  
**Kind**: property

Specifies the find bar container.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var findBarContainer: (any NSTextFinderBarContainer)? { get set }
```

#### Discussion

This property must be set to support the find bar.

When an instance of [`NSTextFinder`](nstextfinder.md) receives a request to display the find bar, it creates a view for the find bar and assigns it to the [`findBarView`](nstextfinderbarcontainer/findbarview.md) property of its `findBarContainer`. This container owns that view, and it’s responsible for making the view visible when the container’s [`isFindBarVisible`](nstextfinderbarcontainer/isfindbarvisible.md) property is `true`. Implement the container’s [`findBarViewDidChangeHeight()`](nstextfinderbarcontainer/findbarviewdidchangeheight().md) method to reposition the find bar when its height changes, which typically occurs in response to a user interaction.

The [`NSScrollView`](nsscrollview.md) class implements [`NSTextFinderBarContainer`](nstextfinderbarcontainer.md) protocol and is the correct place to display the find bar in most circumstances. The container may freely modify the find bar view’s width and origin, but not its height.

If this property is not set, then the find bar cannot be shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/findbarcontainer)*