# CPListImageRowItem

**Framework**: CarPlay  
**Kind**: class

A list template row that displays a series of images.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPListImageRowItem
```

#### Overview

Use `CPListImageRowItem` to display a series of images as a row in a list template. At runtime, use [`CPMaximumNumberOfGridImages`](cpmaximumnumberofgridimages.md) to determine the maximum number of images that the row displays. CarPlay may display fewer images, depending on the width of the vehicle’s primary screen. Provide images that are display-ready, and include light and dark variants of each. See [`init(text:images:)`](cplistimagerowitem/init(text:images:).md) for more information.

You assign a [`handler`](cplistimagerowitem/handler.md) to the list item that CarPlay executes when the user selects the item. You can assign a second handler, [`listImageRowHandler`](cplistimagerowitem/listimagerowhandler.md), which CarPlay calls when the user selects an individual image.

CarPlay doesn’t support custom list item types. Instead, use the `userInfo` property to attach a value to the list item that provides additional context, such as specifying  a model object that corresponds to the item.

## Topics

### Creating a List Image Row Item
- [init(text: String, images: [UIImage])](cplistimagerowitem/init(text:images:).md)
  Creates a list item that displays a row of images.
- [init(text: String, images: [UIImage], imageTitles: [String])](cplistimagerowitem/init(text:images:imagetitles:).md)
  Creates a list item that displays a row of images with a title below each image.
### Managing Content
- [var text: String?](cplistimagerowitem/text.md)
  The list item’s primary text.
- [var gridImages: [UIImage]](cplistimagerowitem/gridimages.md)
  The images that appear in the list item’s image row.
- [func update([UIImage])](cplistimagerowitem/update(_:).md)
  Adds, removes, reorders, or updates the images in the list item’s image row.
- [class var maximumImageSize: CGSize](cplistimagerowitem/maximumimagesize.md)
  The maximum size of an image that an image row can display.
- [let CPMaximumNumberOfGridImages: Int](cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.
### Managing Selection
- [var listImageRowHandler: ((CPListImageRowItem, Int, () -> Void) -> Void)?](cplistimagerowitem/listimagerowhandler.md)
  An optional closure that CarPlay invokes when the user selects an image.
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](cplistimagerowitem/handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.
### Managing Supplementary Information
- [var userInfo: Any?](cplistimagerowitem/userinfo.md)
  An opaque value for the list item.
### Enabling Items
- [var isEnabled: Bool](cplistimagerowitem/isenabled.md)
  A Boolean value that indicates if the item is enabled.
### Initializers
- [init(text: String?, cardElements: [CPListImageRowItemCardElement], allowsMultipleLines: Bool)](cplistimagerowitem/init(text:cardelements:allowsmultiplelines:).md)
  Initialize a list image row item with a text string, an array of @c CPListImageRowItemCardElement and a boolean to allow multiple lines in this row.
- [init(text: String?, condensedElements: [CPListImageRowItemCondensedElement], allowsMultipleLines: Bool)](cplistimagerowitem/init(text:condensedelements:allowsmultiplelines:).md)
  Initialize a list image row item with a text string, an array of @c CPListImageRowItemCondensedElement and a boolean to allow multiple lines in this row.
- [init(text: String?, elements: [CPListImageRowItemRowElement], allowsMultipleLines: Bool)](cplistimagerowitem/init(text:elements:allowsmultiplelines:).md)
  Initialize a list image row item with a text string, an array of @c CPListImageRowItemRowElement and a boolean to allow multiple lines in this row.
- [init(text: String?, gridElements: [CPListImageRowItemGridElement], allowsMultipleLines: Bool)](cplistimagerowitem/init(text:gridelements:allowsmultiplelines:).md)
  Initialize a list image row item with a text string, an array of @c CPListImageRowItemGridElement and a boolean to allow multiple lines in this row.
- [init(text: String?, imageGridElements: [CPListImageRowItemImageGridElement], allowsMultipleLines: Bool)](cplistimagerowitem/init(text:imagegridelements:allowsmultiplelines:).md)
  Initialize a list image row item with a text string, an array of @c CPListImageRowItemImageGridElement and a boolean to allow multiple lines in this row.
### Instance Properties
- [var allowsMultipleLines: Bool](cplistimagerowitem/allowsmultiplelines.md)
  A Boolean value indicating whether the elements should be visible in more than a single line.
- [var elements: [CPListImageRowItemElement]](cplistimagerowitem/elements.md)
  The array of elements used to draw visible elements.
- [var imageTitles: [String]](cplistimagerowitem/imagetitles.md)
  The titles displayed for each image in this image row item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CPListTemplateItem](cplisttemplateitem.md)
- [CPSelectableListItem](cpselectablelistitem.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:).md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [protocol CPSelectableListItem](cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](cplistitem.md)
  A selectable row in a list template.
- [class CPMessageListItem](cpmessagelistitem.md)
  A list template row that represents a conversation or contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem)*