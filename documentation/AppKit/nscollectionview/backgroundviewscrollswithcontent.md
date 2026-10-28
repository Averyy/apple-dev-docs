# backgroundViewScrollsWithContent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the collection view’s background view scrolls with the items and other content.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var backgroundViewScrollsWithContent: Bool { get set }
```

```objc
@property BOOL backgroundViewScrollsWithContent;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md), which means that [`backgroundView`](./backgroundview.md) (if it exists) fills the collection view’s visible area and remains stationary when the collection view’s content is scrolled. When the value of this property is [`true`](../../Swift/true.md), [`backgroundView`](./backgroundview.md) matches the collection view’s frame and scrolls with the collection view’s items and other content.

Changing the value of this property also changes the background view’s parent. When [`backgroundView`](./backgroundview.md) floats behind the scrolling content, it is a sibling of the collection view’s clip view. When it scrolls with the collection view’s content, it is a subview of the collection view.

## See Also

### Configuring the Collection View
- [var delegate: (any NSCollectionViewDelegate)?](./delegate.md)
  The collection view’s delegate object.
- [protocol NSCollectionViewDelegate](../nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [var content: [Any]](./content.md)
  An array that provides data for the collection view.
- [var backgroundView: NSView?](./backgroundview.md)
  The background view placed behind all items and supplementary views.
- [var backgroundColors: [NSColor]!](./backgroundcolors.md)
  An array containing the collection view’s background colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/backgroundviewscrollswithcontent)*