# backgroundColors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the collection view’s background colors.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var backgroundColors: [NSColor]! { get set }
```

```objc
@property (copy, null_resettable) NSArray<NSColor *> * backgroundColors;
```

#### Discussion

This property contains an array of [`NSColor`](../nscolor.md) objects, representing the colors to use when drawing the background grid. Specifying an empty array or `nil` causes the collection view to use the default colors returned by the [`controlAlternatingRowBackgroundColors`](../nscolor/controlalternatingrowbackgroundcolors.md) method.

When a background view is specified for the collection view, the colors in this property are ignored.

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
- [var backgroundViewScrollsWithContent: Bool](./backgroundviewscrollswithcontent.md)
  A Boolean value that indicates whether the collection view’s background view scrolls with the items and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/backgroundcolors)*