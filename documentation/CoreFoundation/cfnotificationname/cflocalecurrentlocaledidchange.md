# cfLocaleCurrentLocaleDidChange

**Framework**: Core Foundation  
**Kind**: property

Identifier for the notification sent if the current locale changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let cfLocaleCurrentLocaleDidChange: CFNotificationName!
```

#### Discussion

This is a local notification posted when the user changes locale information in the System Preferences panel. Keep in mind that there is no order in how notifications are delivered to observers; frameworks or other parts of your code may also be observing this notification to take their own actions, and these may not have occurred at the time you receive the notification.

There is no object or user info for this notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationname/cflocalecurrentlocaledidchange)*