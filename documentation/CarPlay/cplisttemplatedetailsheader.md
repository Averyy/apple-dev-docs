# CPListTemplateDetailsHeader

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A header section that displays rich media content and action buttons above a list of items.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPListTemplateDetailsHeader
```

```objc
@interface CPListTemplateDetailsHeader : NSObject
```

## Overview

A `CPListTemplateDetailsHeader` object stores header content to display at the top of a list interface. You create this type and specify the title and subtitle text, thumbnail image, and optional action buttons you want to display in the header section of your list. CarPlay takes the content you provide and displays it for you, adapting the content automatically to different screen sizes and interface styles.

To add a header to your list interface, create a `CPListTemplateDetailsHeader` and assign it to your [`CPListTemplate`](./cplisttemplate.md) object. After creating the list template object, assign your header to the template’s [`listHeader`](./cplisttemplate/listheader.md) property. If you assign a header to your list template after the template is visible on the vehicle’s display, CarPlay updates the list interface to display the header.

## Topics

### Creating a details header
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons: [CPButton])](./cplisttemplatedetailsheader/init%28thumbnail,title,subtitle,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])](./cplisttemplatedetailsheader/init%28thumbnail,title,subtitle,bodyvariants,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init?(coder: NSCoder)](./cplisttemplatedetailsheader/init%28coder%29.md)
- [class var maximumActionButtonCount: Int](./cplisttemplatedetailsheader/maximumactionbuttoncount.md)
  The maximum number of action buttons the header can display.
- [class var maximumActionButtonSize: CGSize](./cplisttemplatedetailsheader/maximumactionbuttonsize.md)
  The maximum size of the images you use to create action buttons.
### Managing the header’s content
- [var thumbnail: CPThumbnailImage](./cplisttemplatedetailsheader/thumbnail.md)
  The thumbnail image to display in the header.
- [var title: String?](./cplisttemplatedetailsheader/title.md)
  The primary text to display in the header.
- [var subtitle: String?](./cplisttemplatedetailsheader/subtitle.md)
  The text to display in the header below the title.
- [var bodyVariants: [NSAttributedString]](./cplisttemplatedetailsheader/bodyvariants.md)
  An optional array of localized strings to display beneath the subtitle.
- [var actionButtons: [CPButton]](./cplisttemplatedetailsheader/actionbuttons.md)
  An array of action buttons to display in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](./cplisttemplatedetailsheader/wantsadaptivebackgroundstyle.md)
  A Boolean value that indicates whether to apply a custom background style to the header.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CPPlayableItem](./cpplayableitem.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Headers and special cells
- [class CPAssistantCellConfiguration](./cpassistantcellconfiguration.md)
  A type that configures a special row in for performing app-related actions using Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader)*