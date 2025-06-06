# kSecCSGenerateGuestHash

**Framework**: Security  
**Kind**: var

Ask the host to generate the unique binary identifier ([`kSecCodeInfoUnique`](kseccodeinfounique.md)) from the copy on disk at the path given.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSGenerateGuestHash: UInt32 { get }
```

#### Discussion

Ideally, when the host launches the guest code it should bring the signature in the code directory into memory at the same time, create the unique binary identifier by calculating the SHA-1 hash of the signature, and pass it to the [`SecHostCreateGuest`](sechostcreateguest.md) function as the [`kSecGuestAttributeHash`](ksecguestattributehash.md) attribute in the dictionary when it creates a guest. Doing so guarantees that the identifier was made from the same version of the code as was loaded into memory. This identifier can be used by the host and other processes to make sure the code has not been altered, because the hash of the code directory is a unique identifier of a particular instance of the signature. The `kSecCSGenerateGuestHash` flag tells Code Signing Services to fetch the signature from disk and do the calculation itself. Having the system create the identifier from the code on disk is convenient but is not the most secure option because it is possible for an attacker with write access to substitute a different copy of the code directory on disk after the code is loaded into memory but before the system generates the identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccsgenerateguesthash)*