# dislikeCommand

**Framework**: Media Player  
**Kind**: property

The command object for indicating that a user dislikes what is currently playing.

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
var dislikeCommand: MPFeedbackCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for disliking the current track. Use your handler to register the user’s dislike for a track, artist, or whatever is appropriate for your app. You can disable the command if your app does not support it.

In addition to registering a handler, you can use the command object to provide a localized string to communicate what is being liked to the user.

## See Also

- [var ratingCommand: MPRatingCommand](mpremotecommandcenter/ratingcommand.md)
  The command object for rating a media item.
- [var likeCommand: MPFeedbackCommand](mpremotecommandcenter/likecommand.md)
  The command object for indicating that a user likes what is currently playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/dislikecommand)*