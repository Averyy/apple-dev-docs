# CPListImageRowItemElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An abstract class for an element in a row of a list.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemElement
```

```objc
@interface CPListImageRowItemElement : NSObject
```

## Overview

The `CPListImageRowItemElement ` class is an abstract class that defines the shared behavior for row elements. Use properties of this type to access common information about an element, such as the image it displays. You can also change the state of the item to enable or disable interactions.

Row item elements adopt the [`CPPlayableItem`](./cpplayableitem.md) protocol, which adds media-related metadata to each element. Use this metadata to display playback-related information for each element. For example, add duration and elapsed time details to convey someone’s playback progress.

## Topics

### Getting the element’s content
- [var image: UIImage](./cplistimagerowitemelement/image.md)
  The image associated with the element.
- [class var maximumImageSize: CGSize](./cplistimagerowitemelement/maximumimagesize.md)
  The maximum dimensions for the element’s image.
### Describing the image
- [var accessibilityLabel: String?](./cplistimagerowitemelement/accessibilitylabel.md)
  Accessibility text to apply to the element’s image.
### Enabling and disabling the element
- [var isEnabled: Bool](./cplistimagerowitemelement/isenabled.md)
  A Boolean value that indicates whether the item is enabled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPListImageRowItemCardElement](./cplistimagerowitemcardelement.md)
- [CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
- [CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
- [CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
- [CPListImageRowItemRowElement](./cplistimagerowitemrowelement.md)
### Conforms To
- [CPPlayableItem](./cpplayableitem.md)
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

### Common types
- [class CPThumbnailImage](./cpthumbnailimage.md)
  An image that can display overlays and metadata on top of the image.
- [protocol CPSelectableListItem](./cpselectablelistitem.md)
  An interface for responding to selections in list items.
- [protocol CPListTemplateItem](./cplisttemplateitem.md)
  An interface that describes the common properties of all list item types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement)*