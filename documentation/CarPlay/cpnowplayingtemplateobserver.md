# CPNowPlayingTemplateObserver

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

Methods for responding to interactions with buttons in the Now Playing template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPNowPlayingTemplateObserver : NSObjectProtocol
```

```objc
@protocol CPNowPlayingTemplateObserver <NSObject>
```

## Overview

If you enable the Album Artist or Up Next button in the Now Playing interface, use this protocol to respond to interactions with those buttons. Implement this protocol in one of your app’s custom objects, and register the object as an observer using the [`add(_:)`](./cpnowplayingtemplate/add%28_%29.md) method of [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md). For each of the protocol’s methods, provide a response when someone interacts with the button. For example, when someone selects the Album Artist button, update your app’s interface to display the artist information for the currently playing item.

## Topics

### Responding to interactions
- [func nowPlayingTemplateAlbumArtistButtonTapped(CPNowPlayingTemplate)](./cpnowplayingtemplateobserver/nowplayingtemplatealbumartistbuttontapped%28_%29.md)
  Tells the delegate that someone wants to view album artist information.
- [func nowPlayingTemplateUpNextButtonTapped(CPNowPlayingTemplate)](./cpnowplayingtemplateobserver/nowplayingtemplateupnextbuttontapped%28_%29.md)
  Tells the delegate that someone wants to view the Up Next content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Now playing
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [Now Playing supporting types](./now-playing-support.md)
  Add Now Playing buttons to your interface and configure overlays with sports information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver)*