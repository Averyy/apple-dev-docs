# NSUbiquitousKeyValueStoreInitialSyncChange

**Framework**: Foundation  
**Kind**: var

A constant that indicates the initial attempt to load keys and values from iCloud is in progress.

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
var NSUbiquitousKeyValueStoreInitialSyncChange: Int { get }
```

#### Discussion

The system downloads the existing keys and values from iCloud when someone logs into a device using their Apple account. If you try to write a key and value to the iCloud data store while this initial download is in progress, the system generates the [`didChangeExternallyNotification`](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) notification with this key. Schedule the write operations after a delay to give the system time to download the data and ensure the local copies match the truth in iCloud.

## See Also

- [class let didChangeExternallyNotification: NSNotification.Name](nsubiquitouskeyvaluestore/didchangeexternallynotification.md)
  Posted when the value of one or more keys changes due to incoming data from iCloud.
- [let NSUbiquitousKeyValueStoreChangeReasonKey: String](nsubiquitouskeyvaluestorechangereasonkey.md)
  A key that indicates the reason why the key-value store changed.
- [let NSUbiquitousKeyValueStoreChangedKeysKey: String](nsubiquitouskeyvaluestorechangedkeyskey.md)
  A key that indicates which keys changed in the iCloud key-value store.
- [var NSUbiquitousKeyValueStoreServerChange: Int](nsubiquitouskeyvaluestoreserverchange.md)
  A constant that indicates a value changed in iCloud.
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)
  A constant that indicates an attempt to write data exceeded the quota limits.
- [var NSUbiquitousKeyValueStoreAccountChange: Int](nsubiquitouskeyvaluestoreaccountchange.md)
  A constant that indicates the current Apple account changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange)*