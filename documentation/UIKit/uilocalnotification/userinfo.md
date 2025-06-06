# userInfo

**Framework**: UIKit  
**Kind**: property

A dictionary for passing custom information to the notified app.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var userInfo: [AnyHashable : Any]? { get set }
```

#### Discussion

You may add arbitrary key-value pairs to this dictionary. However, the keys and values must be valid [`Property list`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44); if any are not, an exception is raised.

## See Also

- [var applicationIconBadgeNumber: Int](uilocalnotification/applicationiconbadgenumber.md)
  The number to display as the app’s icon badge.
- [var soundName: String?](uilocalnotification/soundname.md)
  The name of the file containing the sound to play when an alert is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/userinfo)*