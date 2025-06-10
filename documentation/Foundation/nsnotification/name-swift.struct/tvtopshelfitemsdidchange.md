# TVTopShelfItemsDidChange

**Framework**: Foundation  
**Kind**: property

A notification to post when your app’s Top Shelf content has changed.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
static let TVTopShelfItemsDidChange: NSNotification.Name
```

#### Discussion

When the content has changed, post a new notification using the default notification center (`[NSNotificationCenter defaultCenter]`). At some point in the future, the system will fetch the new data from your extension. The notification’s parameters are ignored and should be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/tvtopshelfitemsdidchange)*