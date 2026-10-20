# margins

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The amount of empty space (in points) around the grid’s content.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var margins: NSEdgeInsets { get set }
```

```objc
@property NSEdgeInsets margins;
```

#### Discussion

The default value of this property is `NSEdgeInsetsZero`. Changing this property to a new value invalidates the layout.

## See Also

### Specifying the Grid Layout Attributes
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout/margins)*