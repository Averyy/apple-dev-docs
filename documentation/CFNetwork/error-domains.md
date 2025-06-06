# Error Domains

**Framework**: CFNetwork

High-level error domains.

#### Overview

To determine the source of an error, examine the `userInfo` dictionary included in the `CFError` object returned by a function call or call [`CFErrorGetDomain(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFErrorGetDomain(_:)) and pass in the `CFError` object and the domain whose value you want to read.

## Topics

### Constants
- [let kCFErrorDomainCFNetwork: CFString](kcferrordomaincfnetwork.md)
- [let kCFErrorDomainWinSock: CFString](kcferrordomainwinsock.md)

## See Also

- [enum CFNetworkErrors](cfnetworkerrors.md)
  This enumeration contains error codes returned under the error domain [`kCFErrorDomainCFNetwork`](kcferrordomaincfnetwork.md).
- [Error Dictionary Keys](error-dictionary-keys.md)
  Networking-related keys that may be available in a `CFErrorRef` object’s `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/error-domains)*