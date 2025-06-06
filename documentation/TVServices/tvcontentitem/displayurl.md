# displayURL

**Framework**: TV Services  
**Kind**: property

A URL that causes the app which created this content item to display a description screen for the item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var displayURL: URL? { get set }
```

#### Discussion

When the user selects the item, your application is launched if it wasn’t already running and then your [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) delegate is called. If at all possible, your application should immediately display the description of the item without any prompting for other information or displaying any other UI.

## See Also

- [var playURL: URL?](tvcontentitem/playurl.md)
  A URL that causes the app which created this content item to begin playing the item at the user’s current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/displayurl)*