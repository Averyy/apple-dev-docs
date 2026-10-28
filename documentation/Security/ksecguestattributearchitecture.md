# kSecGuestAttributeArchitecture

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a number representing the CPU type under which the guest code is designed to run.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecGuestAttributeArchitecture: CFString
```

```c
extern CFStringRef const kSecGuestAttributeArchitecture;
```

## Discussion

See the ARCH(3) manual page for a list of possible CPU types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecguestattributearchitecture)*