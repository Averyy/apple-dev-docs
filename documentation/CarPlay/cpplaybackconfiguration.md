# CPPlaybackConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

Media metadata you add to audio or video items to support automatic system behaviors.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPPlaybackConfiguration
```

```objc
@interface CPPlaybackConfiguration : NSObject
```

## Overview

When your app displays audio or video content in a list, create `CPPlaybackConfiguration` objects for your list’s rows and row elements to enable automatic system behaviors. Specifically, the system can display playback progress as part of your row or row element’s content. When someone interacts with the item, the system can also display the relevant system interface and automatically start playing the media item. Specify the behaviors you want individually for each item in your list.

Create an instance of this class for each row or row element in your interface that contains playable audio or video content. For each instance you create, enable the behaviors you want and assign the instance to the [`playbackConfiguration`](./cpplayableitem/playbackconfiguration.md) property of the item. You can assign playback configuration objects to [`CPListItem`](./cplistitem.md) objects, to instances of the system-defined [`CPListImageRowItem`](./cplistimagerowitem.md) subclasses, and to the [`CPListTemplateDetailsHeader`](./cplisttemplatedetailsheader.md) type. If you don’t provide a `CPPlaybackConfiguration` object for an item, the system doesn’t provide any automatic behaviors for it.

> **Note**: To determine if video playback is available, check the `CPSessionConfiguration/videoPlaybackSupported` property of the session configuration object.

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpplaybackconfiguration/init%28coder%29.md)
- [init(preferredPresentation: CPPlaybackConfiguration.Presentation, playbackAction: CPPlaybackConfiguration.Action, elapsedTime: CMTime, duration: CMTime)](./cpplaybackconfiguration/init%28preferredpresentation,playbackaction,elapsedtime,duration%29.md)
  Creates a playback configuration object with the specified presentation style, playback action, and media details.
### Instance Properties
- [var duration: CMTime](./cpplaybackconfiguration/duration.md)
  The duration of the media file in seconds.
- [var elapsedTime: CMTime](./cpplaybackconfiguration/elapsedtime.md)
  The elapsed time since the start of playback.
- [var playbackAction: CPPlaybackConfiguration.Action](./cpplaybackconfiguration/playbackaction.md)
  The action to perform on the media item when someone selects it.
- [var preferredPresentation: CPPlaybackConfiguration.Presentation](./cpplaybackconfiguration/preferredpresentation.md)
  The preferred presentation behavior when someone selects the media item.
### Enumerations
- [CPPlaybackConfiguration.Action](./cpplaybackconfiguration/action.md)
  The action to perform when someone selects the item.
- [CPPlaybackConfiguration.Presentation](./cpplaybackconfiguration/presentation.md)
  Constants that specify the presentation style for the media of a selected item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Playback configuration
- [protocol CPPlayableItem](./cpplayableitem.md)
  An interface that adds media-based metadata to items with audio or video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration)*