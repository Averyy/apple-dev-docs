# IKFilterBrowserDefaultInputImage

**Framework**: Quartz  
**Kind**: var

The key for the default input image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let IKFilterBrowserDefaultInputImage: String
```

#### Discussion

The associated value is the [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) object to use as the default input image for the filter preview. Setting the image to `nil` causes Image Kit to use the image supplied by the framework. You can also set the input image and other parameters during the notification [`IKFilterBrowserWillPreviewFilterNotification`](ikfilterbrowserwillpreviewfilternotification.md).

## See Also

- [var IKImageBrowserDropOn: IKImageBrowserDropOperation](ikimagebrowserdropon.md)
  Drop the item on the cell.
- [var IKImageBrowserDropBefore: IKImageBrowserDropOperation](ikimagebrowserdropbefore.md)
  Drop the item before the cell.
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
- [let IKImageBrowserCellsTitleAttributesKey: String](ikimagebrowsercellstitleattributeskey.md)
  A key for  title attribute of an item in the image browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserdefaultinputimage)*