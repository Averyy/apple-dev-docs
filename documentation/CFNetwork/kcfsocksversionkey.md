# kCFSOCKSVersionKey

**Framework**: CFNetwork  
**Kind**: var

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCFSOCKSVersionKey: CFString
```

#### Discussion

If an error of type `kCFSOCKSErrorUnsupportedServerVersion` is returned, querying this key returns the SOCKS version in use by the current connection.

## See Also

- [let kCFURLErrorFailingURLErrorKey: CFString](kcfurlerrorfailingurlerrorkey.md)
  The URL that caused the load to fail as a `CFURLRef` object.
- [let kCFURLErrorFailingURLStringErrorKey: CFString](kcfurlerrorfailingurlstringerrorkey.md)
  The URL that caused the load to fail as a `CFStringRef` object.
- [let kCFGetAddrInfoFailureKey: CFString](kcfgetaddrinfofailurekey.md)
- [let kCFSOCKSStatusCodeKey: CFString](kcfsocksstatuscodekey.md)
- [let kCFSOCKSNegotiationMethodKey: CFString](kcfsocksnegotiationmethodkey.md)
- [let kCFDNSServiceFailureKey: CFString](kcfdnsservicefailurekey.md)
- [let kCFFTPStatusCodeKey: CFString](kcfftpstatuscodekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfsocksversionkey)*