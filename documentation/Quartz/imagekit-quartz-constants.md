# ImageKit Constants

**Framework**: Quartz

## Topics

### Constants
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
- [let IKImageBrowserCellsTitleAttributesKey: String](ikimagebrowsercellstitleattributeskey.md)
  A key for  title attribute of an item in the image browser view.
- [let IKImageBrowserGroupBackgroundColorKey: String](ikimagebrowsergroupbackgroundcolorkey.md)
  A key for the background color of a group.
- [let IKImageBrowserGroupFooterLayer: String](ikimagebrowsergroupfooterlayer.md)
  A key for the header layer of the group.
- [let IKImageBrowserGroupHeaderLayer: String](ikimagebrowsergroupheaderlayer.md)
  A key for the header layer of the group.
- [let IKImageBrowserGroupRangeKey: String](ikimagebrowsergrouprangekey.md)
  A key for the range of a group.
- [let IKImageBrowserGroupStyleKey: String](ikimagebrowsergroupstylekey.md)
  A key for the style of a group.
- [let IKImageBrowserGroupTitleKey: String](ikimagebrowsergrouptitlekey.md)
  A key for the title of a group.
- [let IKImageBrowserSelectionColorKey: String](ikimagebrowserselectioncolorkey.md)
  A key for the color that indicates a selection.
- [var IKImageStateInvalid: IKImageBrowserCellState](ikimagestateinvalid.md)
  The thumbnail is invalid. For example, an unsupported image is provided.
- [var IKImageStateNoImage: IKImageBrowserCellState](ikimagestatenoimage.md)
  Returned until a thumbnail has been created from the represented object.
- [var IKImageStateReady: IKImageBrowserCellState](ikimagestateready.md)
  The receiver’s represented object has been set and the cell is ready to display.
- [let IKOverlayTypeBackground: String](ikoverlaytypebackground.md)
  A background.
- [let IKOverlayTypeImage: String](ikoverlaytypeimage.md)
  An image.
- [let IKPictureTakerAllowsEditingKey: String](ikpicturetakerallowseditingkey.md)
  A key for allowing image editing.
- [let IKPictureTakerAllowsFileChoosingKey: String](ikpicturetakerallowsfilechoosingkey.md)
  A key for allowing the user to choose a file.
- [let IKPictureTakerAllowsVideoCaptureKey: String](ikpicturetakerallowsvideocapturekey.md)
  A key for allowing video capture.
- [let IKPictureTakerImageTransformsKey: String](ikpicturetakerimagetransformskey.md)
  A n image transformation key. The associated value is an `NSDictionary` object that can be serialized.
- [let IKPictureTakerInformationalTextKey: String](ikpicturetakerinformationaltextkey.md)
  A key for informational text. The associated value is an `NSString` or `NSAttributedString` object whose default value is `"Drag Image Here"`.
- [let IKPictureTakerOutputImageMaxSizeKey: String](ikpicturetakeroutputimagemaxsizekey.md)
  A key for the maximum size of the output image. The associated value is an `NSValue` object (`NSSize`).
- [let IKPictureTakerRemainOpenAfterValidateKey: String](ikpicturetakerremainopenaftervalidatekey.md)
  A key that determines if the picture taker UI should remain open after the user selects done.
- [let IKPictureTakerShowAddressBookPicture: String](ikpicturetakershowaddressbookpicture.md)
- [let IKPictureTakerShowAddressBookPictureKey: String](ikpicturetakershowaddressbookpicturekey.md)
  A key for showing the address book picture.
- [let IKPictureTakerShowEffectsKey: String](ikpicturetakershoweffectskey.md)
  A key for showing effects.
- [let IKPictureTakerShowEmptyPicture: String](ikpicturetakershowemptypicture.md)
- [let IKPictureTakerShowEmptyPictureKey: String](ikpicturetakershowemptypicturekey.md)
  A key for showing an empty picture. The associated value is an `NSImage` object. The default value is `nil`. If set to an image, the picture taker automatically shows an image at the end of the Recent Pictures pop-up menu. that means “no picture.”
- [let IKPictureTakerShowRecentPictureKey: String](ikpicturetakershowrecentpicturekey.md)
- [let IKPictureTakerUpdateRecentPictureKey: String](ikpicturetakerupdaterecentpicturekey.md)
  A key for allowing a recent picture to be updated.
- [let IKSlideshowAudioFile: String](ikslideshowaudiofile.md)
  A key specifying the audio file played during the slideshow.
- [let IKSlideshowModeImages: String](ikslideshowmodeimages.md)
  All items in the slideshow are images.
- [let IKSlideshowModeOther: String](ikslideshowmodeother.md)
  There are a mixture of items in the slideshow (image, PDF, text, HTML, and so on).
- [let IKSlideshowModePDF: String](ikslideshowmodepdf.md)
  All items in the slideshow are PDF documents.
- [let IKSlideshowPDFDisplayBox: String](ikslideshowpdfdisplaybox.md)
  A key for the PDF display box.
- [let IKSlideshowPDFDisplayMode: String](ikslideshowpdfdisplaymode.md)
  A key for the PDF display mode.
- [let IKSlideshowPDFDisplaysAsBook: String](ikslideshowpdfdisplaysasbook.md)
  A key for displaying the slideshow as a book. The associated value is a `Boolean` data type.
- [let IKSlideshowScreen: String](ikslideshowscreen.md)
  A key specifying the screen on which the slideshow is displayed.
- [let IKSlideshowStartIndex: String](ikslideshowstartindex.md)
  A key for the slideshow item index. The associated value is an index.
- [let IKSlideshowStartPaused: String](ikslideshowstartpaused.md)
  A key for starting in a paused state. The associated value is a `Boolean` data type.
- [let IKSlideshowWrapAround: String](ikslideshowwraparound.md)
  A key for starting the slideshow over after the last slide shows. The associated value is a `Boolean` data type.
- [let IKToolModeAnnotate: String](iktoolmodeannotate.md)
  The annotation tool.
- [let IKToolModeCrop: String](iktoolmodecrop.md)
  The crop tool.
- [let IKToolModeMove: String](iktoolmodemove.md)
  The move tool.
- [let IKToolModeNone: String](iktoolmodenone.md)
  No tool is set.
- [let IKToolModeRotate: String](iktoolmoderotate.md)
  The rotation tool.
- [let IKToolModeSelect: String](iktoolmodeselect.md)
  The selection tool.
- [let IKToolModeSelectEllipse: String](iktoolmodeselectellipse.md)
  The selection ellipse.
- [let IKToolModeSelectLasso: String](iktoolmodeselectlasso.md)
  The selection lasso.
- [let IKToolModeSelectRect: String](iktoolmodeselectrect.md)
  Same as `IKToolModeSelect`.
- [let IKUIFlavorAllowFallback: String](ikuiflavorallowfallback.md)
  Substitute controls of another size. The associated value is a Boolean value. If the filter cannot provide a view for the requested size and a fallback is allowed, the filter can use controls of a different size.
- [let IKUISizeFlavor: String](ikuisizeflavor.md)
  A key for the size of the controls in a filter view. The associated value  can be  [`IKUISizeMini`](ikuisizemini.md), [`IKUISizeSmall`](ikuisizesmall.md), or  [`IKUISizeRegular`](ikuisizeregular.md).
- [let IKUISizeMini: String](ikuisizemini.md)
  A very small control.
- [let IKUISizeRegular: String](ikuisizeregular.md)
  A standard size control.
- [let IKUISizeSmall: String](ikuisizesmall.md)
  A small control.
- [let IKUImaxSize: String](ikuimaxsize.md)
  The maximum size of a filter view.
- [let IK_ApertureBundleIdentifier: String](ik_aperturebundleidentifier.md)
  The Aperature application—`com.apple.Aperture`.
- [let IK_MailBundleIdentifier: String](ik_mailbundleidentifier.md)
  The Mail application—`com.apple.mail`.
- [let IK_PhotosBundleIdentifier: String](ik_photosbundleidentifier.md)
- [let IK_iPhotoBundleIdentifier: String](ik_iphotobundleidentifier.md)
  The iPhoto application—`com.apple.iPhoto`.
### Deprecated constants
- [let IKPictureTakerCropAreaSizeKey: String](ikpicturetakercropareasizekey.md)
  A key for the cropping area size. The associated value is an `NSValue` object (`NSSize`).
- [let IKPictureTakerShowAddressBookPicture: String](ikpicturetakershowaddressbookpicture.md)
- [let IKPictureTakerShowEmptyPicture: String](ikpicturetakershowemptypicture.md)

## See Also

- [Quartz Enumerations](quartz-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/imagekit-quartz-constants)*