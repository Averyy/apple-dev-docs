# delegate

**Framework**: AppKit  
**Kind**: property

The collection view’s delegate object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
weak var delegate: (any NSCollectionViewDelegate)? { get set }
```

#### Discussion

Use the delegate object to manage the selection and highlighting of items, track the addition and removal of items, and manage drag and drop operations. The object you assign to this property must conform to the [`NSCollectionViewDelegate`](nscollectionviewdelegate.md) protocol. The default value of this property is `nil`.

## See Also

- [protocol NSCollectionViewDelegate](nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [var content: [Any]](nscollectionview/content.md)
  An array that provides data for the collection view.
- [var backgroundView: NSView?](nscollectionview/backgroundview.md)
  The background view placed behind all items and supplementary views.
- [var backgroundColors: [NSColor]!](nscollectionview/backgroundcolors.md)
  An array containing the collection view’s background colors.
- [var backgroundViewScrollsWithContent: Bool](nscollectionview/backgroundviewscrollswithcontent.md)
  A Boolean value that indicates whether the collection view’s background view scrolls with the items and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/delegate)*