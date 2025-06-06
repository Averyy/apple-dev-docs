# TVTopShelfCarouselItem

**Framework**: TV Services  
**Kind**: class

An item containing images, video, and other information that you want to display using a carousel-based interface.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVTopShelfCarouselItem
```

#### Overview

A [`TVTopShelfCarouselItem`](tvtopshelfcarouselitem.md) object offers a more dynamic way to present your content than section-based items. When a carousel item first appears, it displays either a static image or a short looping video as its background. When the navigation focus stops on the item, the system plays the video in the item’s [`previewVideoURL`](tvtopshelfcarouselitem/previewvideourl.md) property.

Create one or more [`TVTopShelfCarouselItem`](tvtopshelfcarouselitem.md) objects and fill them with information about your content. The system determines which properties of the object to display based on the content style. For the [`TVTopShelfCarouselContent.Style.details`](tvtopshelfcarouselcontent/style-swift.enum/details.md) style, the system displays all of the information in your carousel item. For the [`TVTopShelfCarouselContent.Style.actions`](tvtopshelfcarouselcontent/style-swift.enum/actions.md) style, the system focuses on the actions associated with your item. To specify the actions for both styles, use the inherited [`playAction`](tvtopshelfitem/playaction.md) and [`displayAction`](tvtopshelfitem/displayaction.md) properties of the object.

## Topics

### Specifying the Item Details
- [var contextTitle: String?](tvtopshelfcarouselitem/contexttitle.md)
  A localized string describing why the item is shown in the top shelf.
- [var summary: String?](tvtopshelfcarouselitem/summary.md)
  A descriptive summary of a movie or show.
- [var genre: String?](tvtopshelfcarouselitem/genre.md)
  The genre assigned to the movie or show.
- [var duration: TimeInterval](tvtopshelfcarouselitem/duration.md)
  The length of the movie or show, in seconds.
- [var creationDate: Date?](tvtopshelfcarouselitem/creationdate.md)
  The original release date of the content.
### Specifying the Content Previews
- [var cinemagraphURL: URL?](tvtopshelfcarouselitem/cinemagraphurl.md)
  The URL of a looping video to play, without sound, while the preview loads.
- [var previewVideoURL: URL?](tvtopshelfcarouselitem/previewvideourl.md)
  The URL for the content’s trailer or preview.
### Adding Media Badges
- [var mediaOptions: TVTopShelfCarouselItem.MediaOptions](tvtopshelfcarouselitem/mediaoptions-swift.property.md)
  Information about the media format and presentation options.
- [TVTopShelfCarouselItem.MediaOptions](tvtopshelfcarouselitem/mediaoptions-swift.struct.md)
  Constants indicating the item’s audio and video capabilities.
### Adding Custom Attributes
- [var namedAttributes: [TVTopShelfNamedAttribute]](tvtopshelfcarouselitem/namedattributes.md)
  Additional information to display for your content, such as a list of leading actors.
- [class TVTopShelfNamedAttribute](tvtopshelfnamedattribute.md)
  An object you use to display additional information.

## Relationships

### Inherits From
- [TVTopShelfItem](tvtopshelfitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVTopShelfCarouselContent](tvtopshelfcarouselcontent.md)
  A set of items you present using a carousel-style interface in the top shelf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem)*