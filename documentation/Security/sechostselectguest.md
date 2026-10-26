# SecHostSelectGuest

**Framework**: Security  
**Kind**: func  
**Role**: Function

Makes the calling thread the proxy for a specified guest.

**Availability**:
- macOS 10.5+ - Deprecated in 10.6

## Declaration

```c
OSStatus SecHostSelectGuest(SecGuestRef guestRef, SecCSFlags flags);
```

#### Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

#### Discussion

The specified guest must be dynamically valid. This function works both for hosts acting in proxy mode and those acting in dynamic mode. The selected guest setting remains in effect until it is changed or the thread terminates.

This function tells the system that your application is acting on behalf of the selected guest (or on its own behalf if you specify [`kSecNoGuest`](./ksecnoguest.md) for the `guestRef` parameter). This function acts on a per-thread basis; that is, each of your application’s threads can call this function to select a guest for that thread. Thereafter, the system assumes that any action taken by your application on that thread is on behalf of the selected guest. For example, if your application attempts to access the keychain, the system assumes that the selected guest is the application that is attempting to access the keychain and acts accordingly. You can call this function as often as necessary to act on behalf of as many guests as you wish.

Note that if you are using blocks to implement concurrency, you can’t tell which thread your code will be running on. Therefore, you must make this function call at the beginning of each block to be sure that the guest selection is set correctly for the thread.

## Parameters

- `guestRef`: A guest code object identifying the code on whose behalf the calling thread is to act. To indicate that the calling thread will act on its own behalf, rather than for any guest, pass [`kSecNoGuest`](./ksecnoguest.md).
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.

## See Also

### Related Documentation
- [SecHostCreateGuest](./sechostcreateguest.md)
  Creates a new guest and describes its initial properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sechostselectguest)*