# kCFDNSServiceFailureKey

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
let kCFDNSServiceFailureKey: CFString
```

#### Discussion

If an error of type `kCFNetServicesErrorDNSServiceFailure` is returned, querying this key returns the last error returned by the DNS resolver libraries in response to the previous operation. To interpret the results, look up the error codes in `/usr/include/dns_sd.h` or [`DNS Service Discovery C`](https://developer.apple.com/documentation/dnssd/dns-service-discovery-c).

## See Also

- [let kCFURLErrorFailingURLErrorKey: CFString](kcfurlerrorfailingurlerrorkey.md)
  The URL that caused the load to fail as a `CFURLRef` object.
- [let kCFURLErrorFailingURLStringErrorKey: CFString](kcfurlerrorfailingurlstringerrorkey.md)
  The URL that caused the load to fail as a `CFStringRef` object.
- [let kCFGetAddrInfoFailureKey: CFString](kcfgetaddrinfofailurekey.md)
- [let kCFSOCKSStatusCodeKey: CFString](kcfsocksstatuscodekey.md)
- [let kCFSOCKSVersionKey: CFString](kcfsocksversionkey.md)
- [let kCFSOCKSNegotiationMethodKey: CFString](kcfsocksnegotiationmethodkey.md)
- [let kCFFTPStatusCodeKey: CFString](kcfftpstatuscodekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfdnsservicefailurekey)*