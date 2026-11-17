# CPPlayableItem

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

An interface that adds media-based metadata to items with audio or video content.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
protocol CPPlayableItem : NSObjectProtocol
```

```objc
@protocol CPPlayableItem <NSObject>
```

## Overview

In list interfaces, row and row elements adopt this protocol to support audio and video content. This protocol allows items to display playback progress, and it allows the system to perform automatic actions on your app’s behalf. For example, the system can open the appropriate player interface and automatically start playing an item in response to interactions. These behaviors improve the experience of viewing media in CarPlay and minimize the amount of code you need to provide.

Don’t adopt this protocol in custom types you define. The system uses this protocol only with the following types:

[`CPListItem`](./cplistitem.md) [`CPListImageRowItem`](./cplistimagerowitem.md) [`CPListTemplateDetailsHeader`](./cplisttemplatedetailsheader.md)

When creating a list interface with the above items, configure the playback configuration data for each item. This data includes the item’s duration and elapsed time. It also includes the actions you want the system to perform automatically.

## Topics

### Instance Properties
- [var playbackConfiguration: CPPlaybackConfiguration?](./cpplayableitem/playbackconfiguration.md)
  The media-related metadata to associate with the item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [CPListImageRowItemCardElement](./cplistimagerowitemcardelement.md)
- [CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
- [CPListImageRowItemElement](./cplistimagerowitemelement.md)
- [CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
- [CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
- [CPListImageRowItemRowElement](./cplistimagerowitemrowelement.md)
- [CPListItem](./cplistitem.md)
- [CPListTemplateDetailsHeader](./cplisttemplatedetailsheader.md)

## See Also

### Playback configuration
- [class CPPlaybackConfiguration](./cpplaybackconfiguration.md)
  Media metadata you add to audio or video items to support automatic system behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplayableitem)*