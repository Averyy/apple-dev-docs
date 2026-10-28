# previewSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The size of the drag item’s preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var previewSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize previewSize;
```

## Discussion

You might use this property when configuring animations. If the item does not have an associated preview, this property is set to `CGSizeZero`.

## See Also

### Getting the Item Information
- [var sourceIndexPath: IndexPath?](./sourceindexpath.md)
  The index path of the item in the collection view, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropitem/previewsize)*