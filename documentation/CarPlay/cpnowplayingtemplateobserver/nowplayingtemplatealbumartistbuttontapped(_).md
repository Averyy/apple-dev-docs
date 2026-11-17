# nowPlayingTemplateAlbumArtistButtonTapped(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that someone wants to view album artist information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func nowPlayingTemplateAlbumArtistButtonTapped(_ nowPlayingTemplate: CPNowPlayingTemplate)
```

```objc
- (void) nowPlayingTemplateAlbumArtistButtonTapped:(CPNowPlayingTemplate *) nowPlayingTemplate;
```

## Discussion

In your implementation of this method, present or push a new template to display content for the current album, playlist, or podcast.

## Parameters

- `nowPlayingTemplate`: The Now Playing template that originated the request.

## See Also

### Responding to interactions
- [func nowPlayingTemplateUpNextButtonTapped(CPNowPlayingTemplate)](./nowplayingtemplateupnextbuttontapped%28_%29.md)
  Tells the delegate that someone wants to view the Up Next content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver/nowplayingtemplatealbumartistbuttontapped(_:))*