# playURL

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

A URL that causes the app which created this content item to begin playing the item at the user’s current position.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var playURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * playURL;
```

#### Discussion

When the user presses play on the remote, opened, your application is launched if it wasn’t already running and then your [`UIApplication`](../../UIKit/uiapplication.md) delegate is called. If at all possible, your application should immediately begin playing the content without any prompting for other information or displaying any other UI. Your app should start playback at the user’s current position within the content.

## See Also

### Inspecting the Application Launch Properties
- [var displayURL: URL?](./displayurl.md)
  A URL that causes the app which created this content item to display a description screen for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/playurl)*