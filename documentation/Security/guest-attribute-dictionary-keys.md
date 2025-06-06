# Guest Attribute Dictionary Keys

**Framework**: Security

Specify attributes of guest code.

#### Overview

Use these keys in the dictionary you supply as the `attributes` parameter to the [`SecHostCreateGuest`](sechostcreateguest.md), [`SecHostSetGuestStatus`](sechostsetgueststatus.md), and [`SecCodeCopyGuestWithAttributes(_:_:_:_:)`](seccodecopyguestwithattributes(_:_:_:_:).md) functions.

## Topics

### Constants
- [let kSecGuestAttributeArchitecture: CFString](ksecguestattributearchitecture.md)
  A key whose value is a number representing the CPU type under which the guest code is designed to run.
- [let kSecGuestAttributeAudit: CFString](ksecguestattributeaudit.md)
- [let kSecGuestAttributeCanonical: CFString](ksecguestattributecanonical.md)
  A key whose value is the guest code object for that guest.
- [let kSecGuestAttributeDynamicCode: CFString](ksecguestattributedynamiccode.md)
- [let kSecGuestAttributeDynamicCodeInfoPlist: CFString](ksecguestattributedynamiccodeinfoplist.md)
- [let kSecGuestAttributeHash: CFString](ksecguestattributehash.md)
  A key whose value is a data object containing the SHA-1 hash of the code directory.
- [let kSecGuestAttributeMachPort: CFString](ksecguestattributemachport.md)
  Not implemented.
- [let kSecGuestAttributePid: CFString](ksecguestattributepid.md)
  A key whose value is an integer of type `pid_t` representing a process ID (PID), usually of the kernel’s guest.
- [let kSecGuestAttributeSubarchitecture: CFString](ksecguestattributesubarchitecture.md)
  A key whose value is a number representing the CPU subtype under which the guest code is designed to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/guest-attribute-dictionary-keys)*