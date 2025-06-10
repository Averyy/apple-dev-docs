# NSUbiquitousKeyValueStoreInitialSyncChange

**Framework**: Foundation  
**Kind**: var

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

Your attempt to write to key-value storage was discarded because an initial download from iCloud has not yet happened. That is, before you can first write key-value data, the system must ensure that your app’s local, on-disk cache matches the truth in iCloud.

Initial downloads happen the first time a device is connected to an iCloud account, and when a user switches their primary iCloud account.

## See Also

- [var NSUbiquitousKeyValueStoreServerChange: Int](nsubiquitouskeyvaluestoreserverchange.md)
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)
- [var NSUbiquitousKeyValueStoreAccountChange: Int](nsubiquitouskeyvaluestoreaccountchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange)*