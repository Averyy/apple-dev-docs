# nowPlayingTemplateAlbumArtistButtonTapped(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the user tapped the Album-Artist button.

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

When CarPlay calls this method on your observer, you should present or push a new template that displays the content of the current album, playlist or podcast.

## Parameters

- `nowPlayingTemplate`: The template that contains the button that the user tapped.

## See Also

### Responding to User Interactions
- [func nowPlayingTemplateUpNextButtonTapped(CPNowPlayingTemplate)](./nowplayingtemplateupnextbuttontapped%28_%29.md)
  Tells the observer that the user tapped the Up Next button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver/nowplayingtemplatealbumartistbuttontapped(_:))*