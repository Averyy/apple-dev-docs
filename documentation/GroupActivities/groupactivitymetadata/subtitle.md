# subtitle

**Framework**: Group Activities  
**Kind**: property

The localized string that provides additional information about the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var subtitle: String?
```

#### Discussion

Use this string to provide additional descriptive information about the activity. For example, specify the season and episode information for a television-watching activity. Localize the string for the current device. The system displays this string along with the title in the system UI.

## See Also

- [var title: String?](groupactivitymetadata/title.md)
  The localized string to display as the title of your activity.
- [var previewImage: CGImage?](groupactivitymetadata/previewimage.md)
  The image to display for the current activity.
- [var fallbackURL: URL?](groupactivitymetadata/fallbackurl.md)
  A URL that offers participants a way to identify or join the activity from a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/subtitle)*