# Media Library

**Framework**: Media Library  
**Kind**: module

Access read-only collections of the user’s multimedia content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

#### Overview

The Media Library framework provides a read-only Objective-C data model representing a user’s collections of images, audio, and video. The initial access point of the Media Library framework is [`MLMediaLibrary`](mlmedialibrary.md), which loads the user’s media into a hierarchical structure consisting of media sources, groups, and objects.

At the highest level, all content within a media library instance is categorized by media source. Conceptually, a media source respresents a single app, such as iTunes or Aperture. Each source contains a hierarchy of media groups that originates from a root group. These groups consist of media objects—individual files containing a piece of media such as a photo, song, or movie. Only one copy of each object exists within a media library instance, but an object can be referenced by multiple groups from a single source. The structure of the group hierarchy is specific to each media source.

![None](https://docs-assets.developer.apple.com/published/507ce3b1bd48fc99b5188777563bb105/media-1965615%402x.png)

## Topics

### Classes
- [class MLMediaGroup](mlmediagroup.md)
  The `MLMediaGroup` class provides groupings for media objects from a single source of media, such as iTunes or Aperture. The media objects—individual files containing a piece of media such as a photo, song, or movie—are referenced by one or more groups within each media source. These groupings serve as filters, providing hierarchical structure to the collection of objects in each source.
- [class MLMediaLibrary](mlmedialibrary.md)
  The `MLMediaLibrary` class provides an interface for accessing a collection of media objects from various sources. It serves as the initial access point of the Media Library framework.
- [class MLMediaObject](mlmediaobject.md)
  The `MLMediaObject` class describes a single media file, such as a photo, song, or movie. Each media object contains basic metadata including a name, media type, URL, and so on. Additional information about each object is stored in its list of attributes. For a list of possible object attribute keys, see [`Media Object Attribute Keys`](media-object-attribute-keys.md).
- [class MLMediaSource](mlmediasource.md)
  The `MLMediaSource` class identifies a specific provider of media. Conceptually, a media source respresents a single app, such as iTunes or Aperture. Each media source contains multiple groups of media objects—individual files containing a piece of media such as a photo, song, or movie.
### Reference
- [MediaLibrary Constants](medialibrary-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaLibrary)*