# SecHostSelectedGuest

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the handle for the guest currently selected for the calling thread.

**Availability**:
- macOS 10.5+ - Deprecated in 10.6

## Declaration

```c
OSStatus SecHostSelectedGuest(SecCSFlags flags, SecGuestRef *guestRef);
```

#### Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

#### Discussion

This function may be called in either dynamic hosting mode or proxy hosting mode. If the host has more than one guest, it can set a different selected guest for each thread.

## Parameters

- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.
- `guestRef`: On return, the guest code object of the current selected guest for the calling thread. If no guest is active on this thread (that is, the thread is acting for the host), the value returned is [`kSecNoGuest`](./ksecnoguest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sechostselectedguest)*