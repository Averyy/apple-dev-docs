# userInfo

**Framework**: Foundation  
**Kind**: property

Storage for values or objects related to this notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]?
```

#### Discussion

The user information dictionary stores any additional objects that objects receiving the notification might use.

For example, in AppKit, [`NSControl`](https://developer.apple.com/documentation/AppKit/NSControl) objects post the [`textDidChangeNotification`](https://developer.apple.com/documentation/AppKit/NSControl/textDidChangeNotification) whenever the field editor (an [`NSText`](https://developer.apple.com/documentation/AppKit/NSText) object) changes text inside the `NSControl`. This notification provides the `NSControl` object as the notification’s associated object. In order to provide access to the field editor, the `NSControl` object posting the notification adds the field editor to the notification’s user information dictionary. Objects receiving the notification can access the field editor and the `NSControl` object posting the notification as follows:

```swift
func controlTextDidChange(_ notification: Notification) 
{
    if let fieldEditor = notification.userInfo?["NSFieldEditor"] as? NSText,
        let postingObject = notification.object as? NSControl
    {
        // work with the field editor and posting object
    }
}
```

## See Also

- [var name: Notification.Name](notification/name-swift.property.md)
  A tag identifying the notification.
- [var object: Any?](notification/object.md)
  An object that the poster wishes to send to observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notification/userinfo)*