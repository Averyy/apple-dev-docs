# SecHostRemoveGuest

**Framework**: Security  
**Kind**: func  
**Role**: Function

Removes a guest from a host.

**Availability**:
- macOS 10.5+ - Deprecated in 10.6

## Declaration

```c
OSStatus SecHostRemoveGuest(SecGuestRef host, SecGuestRef guest, SecCSFlags flags);
```

## Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

## Discussion

This function removes all memory of the guest-host relationship from the Code Signing Services hosting system. You cannot remove a dedicated guest. The specified guest must have been created using the [`SecHostCreateGuest`](./sechostcreateguest.md) function. If you remove a guest that is also a host, all of the guest’s guests are removed, recursively, as well, even if one or more of those guests are dedicated hosts.

## Parameters

- `host`: The guest code object of the host of the guest. You cannot specify a host of a host here except in the case of a dedicated host. For a dedicated host, the dedicated host is automatically substituted for its guest. See [`kSecCSDedicatedHost`](./kseccsdedicatedhost.md) for a discussion of dedicated hosts.
- `guest`: The guest code object for the guest whose guest relationship you wish to terminate.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.

## See Also

### Related Documentation
- [SecHostCreateGuest](./sechostcreateguest.md)
  Creates a new guest and describes its initial properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sechostremoveguest)*