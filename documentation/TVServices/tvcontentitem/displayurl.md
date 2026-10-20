# displayURL

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

A URL that causes the app which created this content item to display a description screen for the item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var displayURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * displayURL;
```

#### Discussion

When the user selects the item, your application is launched if it wasn’t already running and then your [`UIApplication`](../../UIKit/uiapplication.md) delegate is called. If at all possible, your application should immediately display the description of the item without any prompting for other information or displaying any other UI.

## See Also

### Inspecting the Application Launch Properties
- [var playURL: URL?](./playurl.md)
  A URL that causes the app which created this content item to begin playing the item at the user’s current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/displayurl)*