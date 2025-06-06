# IKUImaxSize

**Framework**: Quartz  
**Kind**: var

The maximum size of a filter view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let IKUImaxSize: String
```

#### Discussion

Controls whose dimensions are the maximum allowable for the filter view.A width or height of `0` indicates that dimension of the view is not restricted. If the size requested is too small, the filter is expected to return a view as small as possible. It is up to the client to verify that the returned view fits into the context.

## See Also

- [var IKImageBrowserDropOn: IKImageBrowserDropOperation](ikimagebrowserdropon.md)
  Drop the item on the cell.
- [var IKImageBrowserDropBefore: IKImageBrowserDropOperation](ikimagebrowserdropbefore.md)
  Drop the item before the cell.
- [let IKFilterBrowserDefaultInputImage: String](ikfilterbrowserdefaultinputimage.md)
  The key for the default input image.
- [let IKFilterBrowserExcludeCategories: String](ikfilterbrowserexcludecategories.md)
  The key for excluding filter categories.
- [let IKFilterBrowserExcludeFilters: String](ikfilterbrowserexcludefilters.md)
  The key for excluding filters.
- [let IKFilterBrowserShowCategories: String](ikfilterbrowsershowcategories.md)
  The key for showing categories. The associated value is a  `BOOL` value that determines if the filter browser should show the category list.
- [let IKFilterBrowserShowPreview: String](ikfilterbrowsershowpreview.md)
  The associated value is a  `BOOL` value that determines if the filter browser should provide a preview.
- [let IKImageBrowserBackgroundColorKey: String](ikimagebrowserbackgroundcolorkey.md)
  A key for the background color of the image browser view.
- [let IKImageBrowserCellBackgroundLayer: String](ikimagebrowsercellbackgroundlayer.md)
  Layer displayed in the background.
- [let IKImageBrowserCellForegroundLayer: String](ikimagebrowsercellforegroundlayer.md)
  Layer displayed in the foreground.
- [let IKImageBrowserCellPlaceHolderLayer: String](ikimagebrowsercellplaceholderlayer.md)
  Layer displayed as a placeholder when an image is not yet available.
- [let IKImageBrowserCellSelectionLayer: String](ikimagebrowsercellselectionlayer.md)
  Layer displayed as the selection.
- [let IKImageBrowserCellsHighlightedTitleAttributesKey: String](ikimagebrowsercellshighlightedtitleattributeskey.md)
  A key for the highlighted title attribute for an item in the image browser view.
- [let IKImageBrowserCellsOutlineColorKey: String](ikimagebrowsercellsoutlinecolorkey.md)
  A key for the outline color for an item in the image browser view.
- [let IKImageBrowserCellsSubtitleAttributesKey: String](ikimagebrowsercellssubtitleattributeskey.md)
  A key for  a subtitle attribute for an item in the image browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikuimaxsize)*