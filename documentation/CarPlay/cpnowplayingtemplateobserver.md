# CPNowPlayingTemplateObserver

**Framework**: CarPlay  
**Kind**: protocol

The methods for responding to the user interacting with the Now Playing template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPNowPlayingTemplateObserver : NSObjectProtocol
```

#### Overview

You use a Now Playing template observer to respond when the user interacts with the Album-Artist and Up Next buttons. The protocol defines methods that CarPlay calls when a user taps these buttons. Use your implementation to provide the appropriate behavior when these events occur. For example, when the user taps the Album-Artist button, you can present a new template that displays the content of the current album, playlist, or podcast.

To register an observer, create an object that implements the `CPNowPlayingTemplateObserver` protocol and then call the Now Playing template’s [`add(_:)`](cpnowplayingtemplate/add(_:).md) method, passing your object as the only parameter.

## Topics

### Responding to User Interactions
- [func nowPlayingTemplateAlbumArtistButtonTapped(CPNowPlayingTemplate)](cpnowplayingtemplateobserver/nowplayingtemplatealbumartistbuttontapped(_:).md)
  Tells the observer that the user tapped the Album-Artist button.
- [func nowPlayingTemplateUpNextButtonTapped(CPNowPlayingTemplate)](cpnowplayingtemplateobserver/nowplayingtemplateupnextbuttontapped(_:).md)
  Tells the observer that the user tapped the Up Next button.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func add(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/add(_:).md)
  Registers an observer that receives Now Playing template events.
- [func remove(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/remove(_:).md)
  Removes an observer from receiving Now Playing template events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver)*