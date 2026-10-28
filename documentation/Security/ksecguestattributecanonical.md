# kSecGuestAttributeCanonical

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is the guest code object for that guest.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecGuestAttributeCanonical: CFString
```

```c
extern CFStringRef const kSecGuestAttributeCanonical;
```

## Discussion

This object plus the process ID ([`kSecGuestAttributePid`](./ksecguestattributepid.md)) uniquely identify the guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecguestattributecanonical)*