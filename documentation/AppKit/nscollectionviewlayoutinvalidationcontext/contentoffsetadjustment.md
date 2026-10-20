# contentOffsetAdjustment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delta value to add to the collection view’s content offset.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var contentOffsetAdjustment: NSPoint { get set }
```

```objc
@property NSPoint contentOffsetAdjustment;
```

#### Discussion

The content offset adjustment shifts the position of content inside the collection view by the specified amount. You use this value to make tweaks based on how you want to present your content. For example, you might use it to ensure that the first line of items is always lined up at the same position in the collection view’s visible rectangle. When making adjustments, you can specify both positive and negative values.

The default value of this property is [`NSZeroSize`](../../Foundation/nszerosize.md).

## See Also

### Invalidating the Content Area
- [var contentSizeAdjustment: NSSize](./contentsizeadjustment.md)
  The delta value to add to the collection view’s content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/contentoffsetadjustment)*