# CPListTemplateDetailsHeader

**Framework**: CarPlay  
**Kind**: class

A header for list templates that displays rich media content with action buttons.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPListTemplateDetailsHeader
```

#### Overview

CPListTemplateDetailsHeader provides a prominent header section for list templates that includes a thumbnail image, title, subtitle, and configurable action buttons. This component is ideal for displaying media items, content details, or featured items at the top of a list template in CarPlay applications.

The header supports:

- A thumbnail image with overlay and progress indicators
- Primary title and subtitle text
- Up to a maximum number of action buttons for user interaction
- Automatic layout and styling appropriate for CarPlay interfaces

This class is designed specifically for CarPlay templates and follows CarPlay design guidelines for typography, spacing, and interaction patterns. The header automatically adapts to different screen sizes and orientations while maintaining optimal readability and touch target sizes.

## Topics

### Initializers
- [init?(coder: NSCoder)](cplisttemplatedetailsheader/init(coder:).md)
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons: [CPButton])](cplisttemplatedetailsheader/init(thumbnail:title:subtitle:actionbuttons:).md)
  Creates a new details header with the specified content and action buttons.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])](cplisttemplatedetailsheader/init(thumbnail:title:subtitle:bodyvariants:actionbuttons:).md)
  Creates a new details header with the specified content and action buttons.
### Instance Properties
- [var actionButtons: [CPButton]](cplisttemplatedetailsheader/actionbuttons.md)
  An array of action buttons displayed in the header.
- [var bodyVariants: [NSAttributedString]](cplisttemplatedetailsheader/bodyvariants.md)
  An optional array of strings, ordered from most to least preferred.
- [var subtitle: String?](cplisttemplatedetailsheader/subtitle.md)
  The secondary subtitle text displayed below the title.
- [var thumbnail: CPThumbnailImage](cplisttemplatedetailsheader/thumbnail.md)
  The thumbnail image displayed in the header.
- [var title: String?](cplisttemplatedetailsheader/title.md)
  The primary title text displayed in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](cplisttemplatedetailsheader/wantsadaptivebackgroundstyle.md)
  A Boolean value that determines whether to use a custom background style.
### Type Properties
- [class var maximumActionButtonCount: Int](cplisttemplatedetailsheader/maximumactionbuttoncount.md)
  The maximum number of action buttons that can be displayed in the header.
- [class var maximumActionButtonSize: CGSize](cplisttemplatedetailsheader/maximumactionbuttonsize.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CPPlayableItem](cpplayableitem.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader)*