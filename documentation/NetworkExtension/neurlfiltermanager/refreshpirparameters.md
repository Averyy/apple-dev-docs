# refreshPIRParameters()

**Framework**: Network Extension  
**Kind**: method

Refetches PIR parameters from the server.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func refreshPIRParameters() async throws
```

#### Discussion

In most cases, you don’t need to perform an explicit refetch because the PIR system on the device refetches PIR parameters from the server periodically to stay up-to-date with the server side. However, in the case of a significant server database change, PIR parameters may change. In this case, you may want to trigger an explicit refresh to make the new set of PIR parameters effective immediately.

The following events can cause PIR parameters to change:

- Re-processing the dataset.
- Changing shard count.
- Changing encryption parameters.
- Changing per-shard cuckoo hash table size (note: per-shard entry count can change while the cuckoo hash table stays fixed size).
- Changing of cuckoo hashing parameters.

## See Also

- [var pirServerURL: URL?](neurlfiltermanager/pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirPrivacyPassIssuerURL: URL?](neurlfiltermanager/pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.
- [var pirAuthenticationToken: String?](neurlfiltermanager/pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func resetPIRCache() async throws](neurlfiltermanager/resetpircache.md)
  Resets the PIR on-device cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/refreshpirparameters())*