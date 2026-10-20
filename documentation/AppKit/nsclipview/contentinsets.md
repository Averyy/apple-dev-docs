# contentInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The distance that the content view is inset from the enclosing scroll view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentInsets: NSEdgeInsets { get set }
```

```objc
@property NSEdgeInsets contentInsets;
```

#### Discussion

When the enclosing scroll view’s [`contentInsets`](../nsscrollview/contentinsets.md) value is nonzero (that is, the value is not {0,0,0,0}), the scroll view sets the frame of its content view to the scroll view’s bounds minus the scroll view’s border, if it has one. (When the [`contentInsets`](../nsscrollview/contentinsets.md) value is equal to zero, the scroll view adjusts its `contentView.frame` to fit inside all the other views the scroll view maintains.) When the value of `contentView.automaticallyAdjustsContentInsets` is [`true`](../../Swift/true.md) (which is the default value), the header, rulers, and other views are overlaid on top of the content view and the scroll view sets the correct [`contentInsets`](../nsscrollview/contentinsets.md) value on the [`contentView`](../nsscrollview/contentview.md). Note that you can animate the clip view when this property changes by calling `[self animator]`.

## See Also

### Accessing the Content Insets
- [var automaticallyAdjustsContentInsets: Bool](./automaticallyadjustscontentinsets.md)
  A Boolean value that indicates if the clip view automatically accounts for other scroll view subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/contentinsets)*