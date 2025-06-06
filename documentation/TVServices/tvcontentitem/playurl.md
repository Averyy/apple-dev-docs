# playURL

**Framework**: TV Services  
**Kind**: property

A URL that causes the app which created this content item to begin playing the item at the user’s current position.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var playURL: URL? { get set }
```

#### Discussion

When the user presses play on the remote, opened, your application is launched if it wasn’t already running and then your [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) delegate is called. If at all possible, your application should immediately begin playing the content without any prompting for other information or displaying any other UI. Your app should start playback at the user’s current position within the content.

## See Also

- [var displayURL: URL?](tvcontentitem/displayurl.md)
  A URL that causes the app which created this content item to display a description screen for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/playurl)*