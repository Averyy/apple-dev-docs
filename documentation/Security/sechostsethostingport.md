# SecHostSetHostingPort

**Framework**: Security  
**Kind**: func  
**Role**: Function

Tells code signing services that the calling code will directly respond to hosting inquiries over the given port.

**Availability**:
- macOS 10.5+ - Deprecated in 10.6

## Declaration

```c
OSStatus SecHostSetHostingPort(mach_port_t hostingPort, SecCSFlags flags);
```

## Mentions

- [Hosting Guest Code](./hosting-guest-code.md)

#### Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

#### Discussion

If you want to use dynamic hosting mode (see [Guest Code](./code-signing-services.md#Guest-Code)), call this function before calling any other code signing services hosting functions. When you call [`SecHostSetHostingPort`](./sechostsethostingport.md), the calling code takes direct responsibility for answering questions about its guests using the hosting IPC services. After you call this function, you cannot call the [`SecHostCreateGuest`](./sechostcreateguest.md), [`SecHostRemoveGuest`](./sechostremoveguest.md), or [`SecHostSetGuestStatus`](./sechostsetgueststatus.md) functions.

The [`SecHostSelectGuest`](./sechostselectguest.md) and [`SecHostSelectedGuest`](./sechostselectedguest.md) functions work after calling this function.

Once you call this function, the calling code must act in dynamic hosting mode; proxy hosting mode is disabled for the lifetime of the calling code.

Dynamic hosting is useful if you have a large host with many guests that are changing status frequently. In that case, it’s more efficient to only respond to requests for information when they’re made than to call the status update functions ([`SecHostCreateGuest`](./sechostcreateguest.md), [`SecHostSetGuestStatus`](./sechostsetgueststatus.md), or [`SecHostRemoveGuest`](./sechostremoveguest.md)) every time something changes. However, dynamic hosting mode is not fully supported by high-level API functions at this time. Unless you have extensive knowledge of Mach messaging and have a particular need to manage your guest code dynamically, it is recommended that you use proxy hosting mode.

## Parameters

- `hostingPort`: A Mach message port with send rights. This port is recorded and handed to parties interested in querying the host about its children.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.

## See Also

### Related Documentation
- [SecHostCreateGuest](./sechostcreateguest.md)
  Creates a new guest and describes its initial properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sechostsethostingport)*