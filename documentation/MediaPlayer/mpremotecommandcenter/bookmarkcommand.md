# bookmarkCommand

**Framework**: Media Player  
**Kind**: property

The command object for indicating that a user wants to remember a media item.

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
var bookmarkCommand: MPFeedbackCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for bookmarking the current track. In your handler, add the track to the user’s list of bookmarks. You can disable the command if your app does not support it.

In addition to registering a handler, you can use the command object to provide a localized string to communicate what is being bookmarked to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/bookmarkcommand)*