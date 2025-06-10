# userInfo

**Framework**: Foundation  
**Kind**: property

The user information dictionary associated with the notification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

#### Discussion

In Objective-C, this may be `nil`.

The user information dictionary stores any additional objects that objects receiving the notification might use.

For example, in AppKit, [`NSControl`](https://developer.apple.com/documentation/AppKit/NSControl) objects post the [`textDidChangeNotification`](https://developer.apple.com/documentation/AppKit/NSControl/textDidChangeNotification) whenever the field editor (an [`NSText`](https://developer.apple.com/documentation/AppKit/NSText) object) changes text inside the `NSControl`. This notification provides the `NSControl` object as the notification’s associated object. In order to provide access to the field editor, the `NSControl` object posting the notification adds the field editor to the notification’s user information dictionary. Objects receiving the notification can access the field editor and the `NSControl` object posting the notification as follows:

```swift
func controlTextDidChange(_ notification: Notification) {
    if let fieldEditor = notification.userInfo?["NSFieldEditor"] as? NSText,
        let postingObject = notification.object as? NSControl {
        // work with the field editor and posting object
    }
}
```

## See Also

- [var name: NSNotification.Name](nsnotification/name-swift.property.md)
  The name of the notification.
- [var object: Any?](nsnotification/object.md)
  The object associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/userinfo)*