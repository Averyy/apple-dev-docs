# Error Dictionary Keys

**Framework**: CFNetwork

Networking-related keys that may be available in a `CFErrorRef` object’s `userInfo` dictionary.

#### Overview

Many network functions return `CFErrorRef` objects. When the error object’s domain is `kCFErrorDomainCFNetwork`, you can query the object for additional information.

For example:

```objc
if (CFEqual(CFErrorGetDomain(err), kCFErrorDomainCFNetwork) && CFErrorGetCode(err) == kCFHostErrorUnknown) {
 
    CFDictionaryRef userInfo = CFErrorCopyUserInfo(err);
 
    CFNumberRef number = (CFNumberRef) CFDictionaryGetValue(userInfo, kCFGetAddrInfoFailureKey);
 
    ...
 
    CFRelease(userInfo);
}
```

## Topics

### Constants
- [let kCFURLErrorFailingURLErrorKey: CFString](kcfurlerrorfailingurlerrorkey.md)
  The URL that caused the load to fail as a `CFURLRef` object.
- [let kCFURLErrorFailingURLStringErrorKey: CFString](kcfurlerrorfailingurlstringerrorkey.md)
  The URL that caused the load to fail as a `CFStringRef` object.
- [let kCFGetAddrInfoFailureKey: CFString](kcfgetaddrinfofailurekey.md)
- [let kCFSOCKSStatusCodeKey: CFString](kcfsocksstatuscodekey.md)
- [let kCFSOCKSVersionKey: CFString](kcfsocksversionkey.md)
- [let kCFSOCKSNegotiationMethodKey: CFString](kcfsocksnegotiationmethodkey.md)
- [let kCFDNSServiceFailureKey: CFString](kcfdnsservicefailurekey.md)
- [let kCFFTPStatusCodeKey: CFString](kcfftpstatuscodekey.md)

## See Also

- [enum CFNetworkErrors](cfnetworkerrors.md)
  This enumeration contains error codes returned under the error domain [`kCFErrorDomainCFNetwork`](kcferrordomaincfnetwork.md).
- [Error Domains](error-domains.md)
  High-level error domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/error-dictionary-keys)*