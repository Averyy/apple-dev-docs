# ALAssetsLibraryChanged

**Framework**: Foundation  
**Kind**: property

Sent when the contents of the assets library have changed from under the app that is using the data.

## Declaration

```swift
static let ALAssetsLibraryChanged: NSNotification.Name
```

#### Discussion

In iOS 4.0, the notification’s [`object`](nsnotification/object.md) is `nil`. In iOS 4.1 and later, the notification object is the library object that posted the notification.

In iOS 6.0 and later, the user information dictionary describes what changed:

- If the user information dictionary is `nil`, reload all assets and asset groups.
- If the user information dictionary an empty dictionary, there is no need to reload assets and asset groups.
- If the user information dictionary is not empty, reload the effected assets and asset groups. For the keys used, see `Notification Keys`.

This notification is sent on an arbitrary thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/alassetslibrarychanged)*