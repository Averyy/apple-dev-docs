# ALAssetsLibraryChangedNotification

**Framework**: Assets Library  
**Kind**: var

Sent when the contents of the assets library have changed from under the app that is using the data.

## Declaration

```swift
extern NSString * const ALAssetsLibraryChangedNotification;
```

#### Discussion

In iOS 4.0, the notification’s [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) is `nil`. In iOS 4.1 and later, the notification object is the library object that posted the notification.

In iOS 6.0 and later, the user information dictionary describes what changed:

- If the user information dictionary is `nil`, reload all assets and asset groups.
- If the user information dictionary an empty dictionary, there is no need to reload assets and asset groups.
- If the user information dictionary is not empty, reload the effected assets and asset groups. For the keys used, see [`Notification Keys`](notification-keys.md).

This notification is sent on an arbitrary thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrarychangednotification)*