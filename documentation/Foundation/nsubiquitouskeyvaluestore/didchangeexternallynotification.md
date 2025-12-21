# didChangeExternallyNotification

**Framework**: Foundation  
**Kind**: property

Posted when the value of one or more keys changes due to incoming data from iCloud.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let didChangeExternallyNotification: NSNotification.Name
```

#### Discussion

If your app is running when iCloud delivers changes from another device, the system generates this notification for your app. Use it to update your app’s content in response to the new data.

The user info dictionary can contain additional data about the reason for the notification:

- When the [`NSUbiquitousKeyValueStoreChangeReasonKey`](nsubiquitouskeyvaluestorechangereasonkey.md) key is present, it indicates the reason why the key-value store changed. The value of this key is one of the constants [`NSUbiquitousKeyValueStoreServerChange`](nsubiquitouskeyvaluestoreserverchange.md), [`NSUbiquitousKeyValueStoreInitialSyncChange`](nsubiquitouskeyvaluestoreinitialsyncchange.md), [`NSUbiquitousKeyValueStoreQuotaViolationChange`](nsubiquitouskeyvaluestorequotaviolationchange.md), or [`NSUbiquitousKeyValueStoreAccountChange`](nsubiquitouskeyvaluestoreaccountchange.md).
- When the [`NSUbiquitousKeyValueStoreChangedKeysKey`](nsubiquitouskeyvaluestorechangedkeyskey.md) key is present, its value is an array of strings, each of which contains the name of a key that changed.

To receive this notification, register for it shortly after launch. Specify the default key-value store object as the object from which you want to receive notifications.

## See Also

- [let NSUbiquitousKeyValueStoreChangeReasonKey: String](nsubiquitouskeyvaluestorechangereasonkey.md)
  A key that indicates the reason why the key-value store changed.
- [let NSUbiquitousKeyValueStoreChangedKeysKey: String](nsubiquitouskeyvaluestorechangedkeyskey.md)
  A key that indicates which keys changed in the iCloud key-value store.
- [var NSUbiquitousKeyValueStoreServerChange: Int](nsubiquitouskeyvaluestoreserverchange.md)
  A constant that indicates a value changed in iCloud.
- [var NSUbiquitousKeyValueStoreInitialSyncChange: Int](nsubiquitouskeyvaluestoreinitialsyncchange.md)
  A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)
  A constant that indicates an attempt to write data exceeded the quota limits.
- [var NSUbiquitousKeyValueStoreAccountChange: Int](nsubiquitouskeyvaluestoreaccountchange.md)
  A constant that indicates the current Apple account changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/didchangeexternallynotification)*