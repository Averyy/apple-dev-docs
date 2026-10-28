# refreshPIRParameters()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Refetches PIR parameters from the server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func refreshPIRParameters() async throws
```

## Discussion

In most cases, you don’t need to perform an explicit refetch because the PIR system on the device refetches PIR parameters from the server periodically to stay up-to-date with the server side. However, in the case of a significant server database change, PIR parameters may change. In this case, you may want to trigger an explicit refresh to make the new set of PIR parameters effective immediately.

The following events can cause PIR parameters to change:

- Re-processing the dataset.
- Changing shard count.
- Changing encryption parameters.
- Changing per-shard cuckoo hash table size (note: per-shard entry count can change while the cuckoo hash table stays fixed size).
- Changing of cuckoo hashing parameters.

## See Also

### Working with a Private Information Retrieval server
- [var pirAuthenticationToken: String?](./pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func resetPIRCache() async throws](./resetpircache%28%29.md)
  Resets the PIR on-device cache.
- [var pirServerURL: URL?](./pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirPrivacyPassIssuerURL: URL?](./pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/refreshpirparameters())*