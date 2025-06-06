# ratingCommand

**Framework**: Media Player  
**Kind**: property

The command object for rating a media item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var ratingCommand: MPRatingCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for rating the current track. In your handler, apply the specified rating to the track. You can disable the command if your app does not support it.

## See Also

- [var likeCommand: MPFeedbackCommand](mpremotecommandcenter/likecommand.md)
  The command object for indicating that a user likes what is currently playing.
- [var dislikeCommand: MPFeedbackCommand](mpremotecommandcenter/dislikecommand.md)
  The command object for indicating that a user dislikes what is currently playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/ratingcommand)*