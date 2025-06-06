# TVContentItem

**Framework**: TV Services  
**Kind**: class

An object that describes either a piece of content or a container for other content items.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVContentItem
```

#### Overview

The exact details of what a content item is are dependent on your app. For example, a content item might be a piece of media or it might provide access to news or other content available to your app.

To create a description of a piece of content, create a content identifier object and then use this object to initialize a new [`TVContentItem`](tvcontentitem.md) object. Then, set any other properties that are appropriate for the object you are creating. Most of the properties are optional, and many properties apply only to certain kinds of content. Inspect an existing [`TVContentItem`](tvcontentitem.md) object to retrieve the media and playback properties, such as the duration of the content or when the content was last played.

## Topics

### Initializing a Content Item
- [init(contentIdentifier: TVContentIdentifier)](tvcontentitem/init(contentidentifier:).md)
  Initializes a new content item.
- [init?(coder: NSCoder)](tvcontentitem/init(coder:).md)
  Returns an object initialized from data in a given unarchiver.
### Reading a Content Item’s Identifier
- [var contentIdentifier: TVContentIdentifier](tvcontentitem/contentidentifier.md)
  The content identifier that uniquely identifies this item.
### Inspecting the General Display Properties
- [var badgeCount: NSNumber?](tvcontentitem/badgecount.md)
  A badging integer for this item.
- [var title: String?](tvcontentitem/title.md)
  The localized string title of the item.
- [var topShelfItems: [TVContentItem]?](tvcontentitem/topshelfitems.md)
  An array of content items that are the items of a section.
### Accessing Image Resources
- [var imageURL: URL?](tvcontentitem/imageurl.md)
  A URL giving the location of the image to be displayed for this content item.
- [func imageURL(forTraits: TVContentItemImageTrait) -> URL?](tvcontentitem/imageurl(fortraits:).md)
  Retrieve the URL for the image that best matches the specified traits.
- [func setImageURL(URL?, forTraits: TVContentItemImageTrait)](tvcontentitem/setimageurl(_:fortraits:).md)
- [struct TVContentItemImageTrait](tvcontentitemimagetrait.md)
  Traits describing the type of image you want.
### Inspecting the Content Properties
- [var creationDate: Date?](tvcontentitem/creationdate.md)
  The date when the content item was created, or the date when it was first broadcast, or some other kind of origination date.
- [var duration: NSNumber?](tvcontentitem/duration.md)
  The amount of time required to play the media to completion.
- [var expirationDate: Date?](tvcontentitem/expirationdate.md)
  The date when the user will no longer be able to access the item.
- [var imageShape: TVContentItemImageShape](tvcontentitem/imageshape.md)
  The intended aspect ratio or shape of the content image.
- [enum TVContentItemImageShape](tvcontentitemimageshape.md)
  An enumerated type that identifies the shape in which the content item should be displayed.
### Inspecting the Playback Properties
- [var currentPosition: NSNumber?](tvcontentitem/currentposition.md)
  The index location, measured in seconds, at which the user last played this item.
- [var hasPlayedToEnd: NSNumber?](tvcontentitem/hasplayedtoend.md)
  A Boolean value indicating whether the user can be considered to have finished this item.
- [var lastAccessedDate: Date?](tvcontentitem/lastaccesseddate.md)
  The date when the user last accessed this item.
### Inspecting the Application Launch Properties
- [var displayURL: URL?](tvcontentitem/displayurl.md)
  A URL that causes the app which created this content item to display a description screen for the item.
- [var playURL: URL?](tvcontentitem/playurl.md)
  A URL that causes the app which created this content item to begin playing the item at the user’s current position.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class TVContentIdentifier](tvcontentidentifier.md)
  An object that uniquely identifies media content in either a single piece or a collection.
- [func TVTopShelfImageSize(shape: TVContentItemImageShape, style: TVTopShelfContentStyle) -> CGSize](tvtopshelfimagesize(shape:style:).md)
  Returns the ideal size for an image, according to its particular shape and style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem)*