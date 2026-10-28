# NSURLCredentialStorageChanged

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification posted when the set of stored credentials changes.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Notification is never posted

## Declaration

```swift
static let NSURLCredentialStorageChanged: NSNotification.Name
```

```c
extern NSNotificationName const NSURLCredentialStorageChangedNotification;
```

## Discussion

The notification’s [`object`](../../notification/object.md) is the [`URLCredentialStorage`](../../urlcredentialstorage.md) instance that changed. This notification does not contain a [`userInfo`](../../notification/userinfo.md) dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsurlcredentialstoragechanged)*