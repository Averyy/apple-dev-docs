# MLMediaSource

**Framework**: Media Library  
**Kind**: class

The `MLMediaSource` class identifies a specific provider of media. Conceptually, a media source respresents a single app, such as iTunes or Aperture. Each media source contains multiple groups of media objects—individual files containing a piece of media such as a photo, song, or movie.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
class MLMediaSource
```

#### Overview

The structure of the group hierarchy is specific to each media source, but all sources have certain commonalities. For example, every source has a single root media group, which contains all groups and objects within that source. It is the highest-level parent group in the hierarchy and each of its descendant groups contains its own subgroups and their objects. All groups have a reference to their parent within the hierarchy. A group with no descendants contains only its own objects. If a media group does not contain any objects, it is not visible in the hierarchy.

Every media source has a unique media source identifier within a single media library instance. For a list of possible media source identifiers, see [`Media Source Identifiers`](media-source-identifiers.md).

All `MLMediaSource` properties are read-only, so this information can be accessed but not altered.

## Topics

### Identifying the Source
- [var mediaSourceIdentifier: String](mlmediasource/mediasourceidentifier.md)
  A unique identifier for the media source.
- [var mediaLibrary: MLMediaLibrary?](mlmediasource/medialibrary.md)
  A pointer to the media library instance that loaded this media source.
### Accessing Source Attributes
- [var attributes: [String : Any]](mlmediasource/attributes.md)
  A list of attributes describing the media source.
### Accessing the Root Media Group
- [var rootMediaGroup: MLMediaGroup?](mlmediasource/rootmediagroup.md)
  The base media group in the media source that contains all other groups within the source as descendant elements.
### Accessing Media
- [func mediaGroup(forIdentifier: String) -> MLMediaGroup?](mlmediasource/mediagroup(foridentifier:).md)
  Returns the media group with the specified identifier.
- [func mediaGroups(forIdentifiers: [String]) -> [String : MLMediaGroup]](mlmediasource/mediagroups(foridentifiers:).md)
  Returns the media groups with the specified identifiers.
- [func mediaObject(forIdentifier: String) -> MLMediaObject?](mlmediasource/mediaobject(foridentifier:).md)
  Returns the media object with the specified identifier.
- [func mediaObjects(forIdentifiers: [String]) -> [String : MLMediaObject]](mlmediasource/mediaobjects(foridentifiers:).md)
  Returns the media objects with the specified identifiers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLMediaGroup](mlmediagroup.md)
  The `MLMediaGroup` class provides groupings for media objects from a single source of media, such as iTunes or Aperture. The media objects—individual files containing a piece of media such as a photo, song, or movie—are referenced by one or more groups within each media source. These groupings serve as filters, providing hierarchical structure to the collection of objects in each source.
- [class MLMediaLibrary](mlmedialibrary.md)
  The `MLMediaLibrary` class provides an interface for accessing a collection of media objects from various sources. It serves as the initial access point of the Media Library framework.
- [class MLMediaObject](mlmediaobject.md)
  The `MLMediaObject` class describes a single media file, such as a photo, song, or movie. Each media object contains basic metadata including a name, media type, URL, and so on. Additional information about each object is stored in its list of attributes. For a list of possible object attribute keys, see [`Media Object Attribute Keys`](media-object-attribute-keys.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource)*