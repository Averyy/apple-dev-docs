# NSURLCredentialStorageChanged

**Framework**: Foundation  
**Kind**: property

A notification posted when the set of stored credentials changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSURLCredentialStorageChanged: NSNotification.Name
```

#### Discussion

The notification’s [`object`](notification/object.md) is the [`URLCredentialStorage`](urlcredentialstorage.md) instance that changed. This notification does not contain a [`userInfo`](notification/userinfo.md) dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsurlcredentialstoragechanged)*