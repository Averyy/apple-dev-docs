# NSUbiquitousKeyValueStoreAccountChange

**Framework**: Foundation  
**Kind**: var

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var NSUbiquitousKeyValueStoreAccountChange: Int { get }
```

#### Discussion

The user has changed the primary iCloud account. The keys and values in the local key-value store have been replaced with those from the new account, regardless of the relative timestamps.

## See Also

- [var NSUbiquitousKeyValueStoreServerChange: Int](nsubiquitouskeyvaluestoreserverchange.md)
- [var NSUbiquitousKeyValueStoreInitialSyncChange: Int](nsubiquitouskeyvaluestoreinitialsyncchange.md)
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreaccountchange)*