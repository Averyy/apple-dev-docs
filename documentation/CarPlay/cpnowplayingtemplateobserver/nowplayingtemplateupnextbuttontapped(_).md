# nowPlayingTemplateUpNextButtonTapped(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that someone wants to view the Up Next content.

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

## Discussion

In your implementation of this method, push a [`CPListTemplate`](../cplisttemplate.md) object onto your interface and fill it with the upcoming or queued content. Don’t push other types of templates.

## Parameters

- `nowPlayingTemplate`: The Now Playing template that originated the request.

## See Also

### Responding to interactions
- [func nowPlayingTemplateAlbumArtistButtonTapped(CPNowPlayingTemplate)](./nowplayingtemplatealbumartistbuttontapped%28_%29.md)
  Tells the delegate that someone wants to view album artist information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplateobserver/nowplayingtemplateupnextbuttontapped(_:))*