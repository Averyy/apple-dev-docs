# nowPlayingTemplateUpNextButtonTapped(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the user tapped the Up Next button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func nowPlayingTemplateUpNextButtonTapped(_ nowPlayingTemplate: CPNowPlayingTemplate)
```

```objc
- (void) nowPlayingTemplateUpNextButtonTapped:(CPNowPlayingTemplate *) nowPlayingTemplate;
```

#### Discussion

When CarPlay calls this method on your observer, you should push an instance of [`CPListTemplate`](../cplisttemplate.md)—other template types are not supported when Now Playing is the visible template—on to your navigation stack that displays a list of upcoming or queued content.

## Parameters

- `nowPlayingTemplate`: The template that contains the button that the user tapped.

## See Also

### Responding to User Interactions
- [func nowPlayingTemplateAlbumArtistButtonTapped(CPNowPlayingTemplate)](./nowplayingtemplatealbumartistbuttontapped%28_%29.md)
  Tells the observer that the user tapped the Album-Artist button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver/nowplayingtemplateupnextbuttontapped(_:))*