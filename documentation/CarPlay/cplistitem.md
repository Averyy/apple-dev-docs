# CPListItem

**Framework**: CarPlay  
**Kind**: class

A selectable row in a list template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPListItem
```

#### Overview

A list item manages the content of a single row in a list template. CarPlay manages the layout of a list item and may adjust its layout to allow for the display of auxiliary content, such as an accessory or a Now Playing indicator. A list item can display primary and secondary text and an image. It can also show an accessory or custom accessory image, and one of several indicators that the system provides.

You assign a [`handler`](cplistitem/handler.md) to a list item that CarPlay executes when the user selects the item. The handler receives the item and a closure that you must call after you finish processing the selection.

CarPlay doesn’t support custom list item types. Instead, use the [`userInfo`](cplistitem/userinfo.md) property to attach a value to the list item that provides additional context, such as specifying  a model object that corresponds to the item.

## Topics

### Creating a List Item
- [init(text: String?, detailText: String?)](cplistitem/init(text:detailtext:).md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?)](cplistitem/init(text:detailtext:image:).md)
  Creates a list item with primary text, secondary text, and an image.
- [init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)](cplistitem/init(text:detailtext:image:accessoryimage:accessorytype:).md)
  Creates a list item that displays an accessory beside its content.
### Managing Configuration
- [var isEnabled: Bool](cplistitem/isenabled.md)
  A Boolean value that indicates if the item is enabled.
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](cplistitem/handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.
- [var userInfo: Any?](cplistitem/userinfo.md)
  An opaque value for the list item.
### Managing Accessories
- [var accessoryType: CPListItemAccessoryType](cplistitem/accessorytype.md)
  The accessory that the list item displays in its trailing region.
- [enum CPListItemAccessoryType](cplistitemaccessorytype.md)
  The accessory types that a list item can display.
- [var accessoryImage: UIImage?](cplistitem/accessoryimage.md)
  The image that the list item displays in its trailing region.
- [func setAccessoryImage(UIImage?)](cplistitem/setaccessoryimage(_:).md)
  Updates the list item’s accessory image.
### Managing Content
- [var text: String?](cplistitem/text.md)
  The list item’s primary text.
- [func setText(String)](cplistitem/settext(_:).md)
  Updates the list item’s primary text.
- [var detailText: String?](cplistitem/detailtext.md)
  The list item’s secondary text.
- [func setDetailText(String?)](cplistitem/setdetailtext(_:).md)
  Updates the list item’s secondary text.
- [var image: UIImage?](cplistitem/image.md)
  The image that the list item displays in its leading region.
- [func setImage(UIImage?)](cplistitem/setimage(_:).md)
  Updates the list item’s image.
- [class var maximumImageSize: CGSize](cplistitem/maximumimagesize.md)
  The maximum size of a list item’s image and accessory image.
### Managing Playback Information
- [var isExplicitContent: Bool](cplistitem/isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var isPlaying: Bool](cplistitem/isplaying.md)
  A Boolean value that determines whether the list item displays its Now Playing indicator.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](cplistitem/playingindicatorlocation.md)
  The location where the list item displays its Now Playing indicator.
- [enum CPListItemPlayingIndicatorLocation](cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var playbackProgress: CGFloat](cplistitem/playbackprogress.md)
  The playback progress status for the content that the list item represents.
### Managing the Assistant Cell
- [CPListItem.AssistantCellPosition](cplistitem/assistantcellposition.md)
  Constants to specify the position of the assistant cell.
- [CPListItem.AssistantCellVisibility](cplistitem/assistantcellvisibility.md)
  Constants to specify the visibility of the assistant cell.
### Deprecated
- [Deprecated Symbols](cplistitem-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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
- [class CPListImageRowItem](cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](cpmessagelistitem.md)
  A list template row that represents a conversation or contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem)*