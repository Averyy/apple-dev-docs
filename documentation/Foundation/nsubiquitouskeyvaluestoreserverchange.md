# NSUbiquitousKeyValueStoreServerChange

**Framework**: Foundation  
**Kind**: var

A constant that indicates a value changed in iCloud.

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
var NSUbiquitousKeyValueStoreServerChange: Int { get }
```

#### Discussion

This type of change occurs when another instance of your app changes the value on a different device.

## See Also

- [class let didChangeExternallyNotification: NSNotification.Name](nsubiquitouskeyvaluestore/didchangeexternallynotification.md)
  Posted when the value of one or more keys changes due to incoming data from iCloud.
- [let NSUbiquitousKeyValueStoreChangeReasonKey: String](nsubiquitouskeyvaluestorechangereasonkey.md)
  A key that indicates the reason why the key-value store changed.
- [let NSUbiquitousKeyValueStoreChangedKeysKey: String](nsubiquitouskeyvaluestorechangedkeyskey.md)
  A key that indicates which keys changed in the iCloud key-value store.
- [var NSUbiquitousKeyValueStoreInitialSyncChange: Int](nsubiquitouskeyvaluestoreinitialsyncchange.md)
  A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)
  A constant that indicates an attempt to write data exceeded the quota limits.
- [var NSUbiquitousKeyValueStoreAccountChange: Int](nsubiquitouskeyvaluestoreaccountchange.md)
  A constant that indicates the current Apple account changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreserverchange)*