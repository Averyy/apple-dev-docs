# previewImage

**Framework**: Group Activities  
**Kind**: property

The image to display for the current activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var previewImage: CGImage?
```

#### Discussion

Use this property to specify an image for the activity. For example, you might display a movie poster for a movie-watching activity. The system scales the image as needed and displays it with the rest of the activity information.

## See Also

- [var title: String?](groupactivitymetadata/title.md)
  The localized string to display as the title of your activity.
- [var subtitle: String?](groupactivitymetadata/subtitle.md)
  The localized string that provides additional information about the activity.
- [var fallbackURL: URL?](groupactivitymetadata/fallbackurl.md)
  A URL that offers participants a way to identify or join the activity from a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/previewimage)*