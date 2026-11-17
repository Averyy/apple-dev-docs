# CPListImageRowItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A row type that displays multiple sub-elements horizontally in a variety of styles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPListImageRowItem
```

```objc
@interface CPListImageRowItem : NSObject
```

## Overview

Create a `CPListImageRowItem` to display image-based content in the rows of your list interface. Each `CPListImageRowItem` represents a single row of content and displays one or more images side-by-side, giving the row a more grid-like appearance. You specify the images in each row using row elements, which are subclasses of `CPListImageRowItemElement`. Each row element subclass defines a unique visual style to apply to the image. You use elements to represent part of your app’s content. For example, a music app might display a row for each playlist and fill the row with elements that represent albums in the playlist.

Create one or more `CPListImageRowItem` types when building the content for your list interface, configure it with elements, and add them to a [`CPListSection`](./cplistsection.md) object. For each element in the row, specify the image to display and any other relevant content. Use the same type for all elements in a single row. Configure the new row with optional closures if you want to respond when someone interacts with the row or one of its elements. Associate any app-specific data with the row using the [`userInfo`](./cplistitem/userinfo.md) property.

Use one of the following types to specify the elements of a row:

- **[`CPListImageRowItemRowElement`](./cplistimagerowitemrowelement.md)**: The type displays an image with some descriptive text.
- **[`CPListImageRowItemCardElement`](./cplistimagerowitemcardelement.md)**: The type displays an image and text inside a card-like shape.
- **[`CPListImageRowItemCondensedElement`](./cplistimagerowitemcondensedelement.md)**: The type displays an image and text in a vertically condensed shape.
- **[`CPListImageRowItemGridElement`](./cplistimagerowitemgridelement.md)**: The type displays an image with a border shape.
- **[`CPListImageRowItemImageGridElement`](./cplistimagerowitemimagegridelement.md)**: The type displays text and an image with a border shape.

Rows support a variable number of items, either on a single line or spread across multiple lines. The [`CPMaximumNumberOfGridImages`](./cpmaximumnumberofgridimages.md) constant defines the maximum number of items you can include in a single row. If the row supports multiple lines, CarPlay adds extra lines as needed until it displays the items you provided. If the row supports only a single line, CarPlay displays as many elements as it can fit into one line and ignores the rest. Configure a single- or multi-line layout when initializing the row.

To create a simpler layout with only one item per row, use the [`CPListItem`](./cplistitem.md) type instead.

## Topics

### Creating a list image row item
- [init(text: String?, elements: [CPListImageRowItemRowElement], allowsMultipleLines: Bool)](./cplistimagerowitem/init%28text,elements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and row elements.
- [init(text: String?, cardElements: [CPListImageRowItemCardElement], allowsMultipleLines: Bool)](./cplistimagerowitem/init%28text,cardelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and card-style elements.
- [init(text: String?, condensedElements: [CPListImageRowItemCondensedElement], allowsMultipleLines: Bool)](./cplistimagerowitem/init%28text,condensedelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and condensed-height elements.
- [init(text: String?, gridElements: [CPListImageRowItemGridElement], allowsMultipleLines: Bool)](./cplistimagerowitem/init%28text,gridelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and grid elements.
- [init(text: String?, imageGridElements: [CPListImageRowItemImageGridElement], allowsMultipleLines: Bool)](./cplistimagerowitem/init%28text,imagegridelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and image grid elements.
### Managing the row’s content
- [var text: String?](./cplistimagerowitem/text.md)
  The row’s primary text.
- [var elements: [CPListImageRowItemElement]](./cplistimagerowitem/elements.md)
  The elements to display in the row.
- [var allowsMultipleLines: Bool](./cplistimagerowitem/allowsmultiplelines.md)
  A Boolean value that indicates whether the row displays elements on more than one line.
- [var userInfo: Any?](./cplistimagerowitem/userinfo.md)
  App-specific data you associate with the item.
- [let CPMaximumNumberOfGridImages: Int](./cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.
### Responding to interactions
- [var listImageRowHandler: ((CPListImageRowItem, Int, () -> Void) -> Void)?](./cplistimagerowitem/listimagerowhandler.md)
  The closure to run when someone interacts with one of the elements in the row.
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./cplistimagerowitem/handler.md)
  The closure to run when someone interacts with any part of the row.
### Enabling and disabling the row
- [var isEnabled: Bool](./cplistimagerowitem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
### Deprecated
- [init(text: String, images: [UIImage])](./cplistimagerowitem/init%28text,images%29.md)
  Initialize a list image row item with a text string and an array of @c UIImage for the grid of images.
- [init(text: String, images: [UIImage], imageTitles: [String])](./cplistimagerowitem/init%28text,images,imagetitles%29.md)
  Initialize a list image row item with a text string, an array of @c UIImage for the grid of images, and an array of @c NSString titles, one displayed below each image.
- [var gridImages: [UIImage]](./cplistimagerowitem/gridimages.md)
  Read-only access to the grid images shown in a row in the cell.
- [var imageTitles: [String]](./cplistimagerowitem/imagetitles.md)
  The titles displayed for each image in this image row item.
- [class var maximumImageSize: CGSize](./cplistimagerowitem/maximumimagesize.md)
  The expected image size for the grid images in your @c CPListImageRowItem. Images provided will be resized to this size.
- [func update([UIImage])](./cplistimagerowitem/update%28_%29.md)
  Update the images displayed in this image row item. If this image row item is already displayed in a list template, this image row item will be automatically reloaded.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CPListTemplateItem](./cplisttemplateitem.md)
- [CPSelectableListItem](./cpselectablelistitem.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Lists
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPListSection](./cplistsection.md)
  A container that groups related items in a list interface.
- [class CPListItem](./cplistitem.md)
  A selectable row in a list interface.
- [Supporting types for lists](./list-content.md)
  Create sections, single-line items, multi-element rows, headers, and other content for your list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem)*