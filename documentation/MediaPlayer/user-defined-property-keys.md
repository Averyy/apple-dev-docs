# User-defined property keys

**Framework**: Media Player

Properties for obtaining user-defined metadata for a media item.

#### Overview

Obtain user-defined metadata for a media item by calling the [`value(forProperty:)`](mpmediaentity/value(forproperty:).md) method with these property keys. Don’t use user-defined properties to build media property predicates.

## Topics

### User-defined property keys
- [let MPMediaItemPropertySkipCount: String](mpmediaitempropertyskipcount.md)
  The number of times the user has skipped playing the item.
- [let MPMediaItemPropertyRating: String](mpmediaitempropertyrating.md)
  The user-specified rating of the object in the range `[0...5]`, where a value of 5 indicates the most favorable rating.
- [let MPMediaItemPropertyLastPlayedDate: String](mpmediaitempropertylastplayeddate.md)
  The most recent calendar date on which the user played the media item.
- [let MPMediaItemPropertyUserGrouping: String](mpmediaitempropertyusergrouping.md)
  Corresponds to the “Grouping” field in the Info tab in the Get Info dialog in iTunes.
- [let MPMediaItemPropertyBookmarkTime: String](mpmediaitempropertybookmarktime.md)
  The user’s place in the media item the most recent time it was played.
- [let MPMediaItemPropertyDateAdded: String](mpmediaitempropertydateadded.md)
  The date the media item was added to the user’s Media library.

## See Also

- [struct MPMediaType](mpmediatype.md)
  The properties for defining the type for a media item.
- [General media item property keys](general-media-item-property-keys.md)
  System-defined properties for obtaining the metadata for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/user-defined-property-keys)*