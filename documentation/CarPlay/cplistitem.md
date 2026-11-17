# CPListItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A selectable row in a list interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPListItem
```

```objc
@interface CPListItem : NSObject
```

## Overview

A `CPListItem` object manages the content for a single row in a list interface. The row contains primary and secondary text elements and an image to describe one piece of your app’s content. For example, a row of this type might describe a single song, album, or playlist. CarPlay handles the presentation of the data you provide, adjusting the row’s layout automatically to accommodate additional elements such as an accessory or Now Playing indicator.

Create one or more `CPListItem` objects when building the content for your list interface, and add them to a [`CPListSection`](./cplistsection.md) object. Specify the text and optional image and accessory information for your row initially, and add an optional [`handler`](./cplistitem/handler.md) to respond when someone selects the row. If your row represents media content, you can also configure any playback-related information using the properties of this type. If you want to associate app-specific data with the row, put that content into the provided [`userInfo`](./cplistitem/userinfo.md) property.

Use this type for simple lists in which each row corresponds to a single data item or selectable choice in your app. To build a more information-dense interface, create rows using the [`CPListImageRowItem`](./cplistimagerowitem.md) type instead.

## Topics

### Creating a list item
- [init(text: String?, detailText: String?)](./cplistitem/init%28text,detailtext%29.md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?)](./cplistitem/init%28text,detailtext,image%29.md)
  Creates a list item with primary text, secondary text, and an image.
- [init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)](./cplistitem/init%28text,detailtext,image,accessoryimage,accessorytype%29.md)
  Creates a list item that displays an accessory beside its content.
### Managing the row’s content
- [var text: String?](./cplistitem/text.md)
  The primary text for the list item.
- [var detailText: String?](./cplistitem/detailtext.md)
  The secondary text for the list item.
- [var image: UIImage?](./cplistitem/image.md)
  The image to display on the leading edge of the cell.
- [func setText(String)](./cplistitem/settext%28_%29.md)
  Updates the primary text of the list item.
- [func setDetailText(String?)](./cplistitem/setdetailtext%28_%29.md)
  Updates the secondary text of the list item.
- [func setImage(UIImage?)](./cplistitem/setimage%28_%29.md)
  Updates the leading image of the list item.
- [var userInfo: Any?](./cplistitem/userinfo.md)
  App-specific data you associate with the item.
- [class var maximumImageSize: CGSize](./cplistitem/maximumimagesize.md)
  The maximum dimensions for the list item images.
### Responding to interactions
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./cplistitem/handler.md)
  The closure to run when someone interacts with any part of the list item.
- [var isEnabled: Bool](./cplistitem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
### Managing accessories
- [var accessoryType: CPListItemAccessoryType](./cplistitem/accessorytype.md)
  The standard accessory type to display on the trailing edge of the list item.
- [var accessoryImage: UIImage?](./cplistitem/accessoryimage.md)
  The custom accessory image to display on the trailing edge of the list item.
- [func setAccessoryImage(UIImage?)](./cplistitem/setaccessoryimage%28_%29.md)
  The custom accessory image to display on the trailing edge of the list item.
- [enum CPListItemAccessoryType](./cplistitemaccessorytype.md)
  The standard image types a list item can display in its accessory region.
### Managing playback information
- [var isPlaying: Bool](./cplistitem/isplaying.md)
  A Boolean value that indicates whether the list item displays the Now Playing indicator.
- [var playbackProgress: CGFloat](./cplistitem/playbackprogress.md)
  The current playback progress for a media item.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](./cplistitem/playingindicatorlocation.md)
  The placement of the Now Playing indicator in the list item’s row.
- [enum CPListItemPlayingIndicatorLocation](./cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var isExplicitContent: Bool](./cplistitem/isexplicitcontent.md)
  A Boolean value that indicates whether the list item displays an explicit content indicator.
### Deprecated
- [init(text: String?, detailText: String?, image: UIImage?, showsDisclosureIndicator: Bool)](./cplistitem/init%28text,detailtext,image,showsdisclosureindicator%29.md)
  Initialize a list item with text, detailtext, an image, and a disclosure indicator.
- [var showsDisclosureIndicator: Bool](./cplistitem/showsdisclosureindicator.md)
  If YES, a cell displaying this list item will render with a disclosure indicator in the trailing side of the cell.
- [var showsExplicitLabel: Bool](./cplistitem/showsexplicitlabel.md)
  If YES, a cell displaying this list item will render with an explicit label to the trailing edge of the text

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CPListTemplateItem](./cplisttemplateitem.md)
- [CPPlayableItem](./cpplayableitem.md)
- [CPSelectableListItem](./cpselectablelistitem.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Lists
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPListSection](./cplistsection.md)
  A container that groups related items in a list interface.
- [class CPListImageRowItem](./cplistimagerowitem.md)
  A row type that displays multiple sub-elements horizontally in a variety of styles.
- [Supporting types for lists](./list-content.md)
  Create sections, single-line items, multi-element rows, headers, and other content for your list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem)*