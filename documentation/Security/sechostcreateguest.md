# SecHostCreateGuest

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a new guest and describes its initial properties.

**Availability**:
- macOS 10.5+ - Deprecated in 10.6

## Declaration

```c
OSStatus SecHostCreateGuest(SecGuestRef host, uint32_t status, CFURLRef path, CFDictionaryRef attributes, SecCSFlags flags, SecGuestRef *newGuest);
```

## Mentions

- [Hosting Guest Code](./hosting-guest-code.md)

## Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

## Discussion

Code that calls this function becomes a code host operating in proxy hosting mode. Subsequently, Code Signing Services caches information about guest code provided by the host when it calls the [`SecHostCreateGuest`](./sechostcreateguest.md), [`SecHostSetGuestStatus`](./sechostsetgueststatus.md), and [`SecHostRemoveGuest`](./sechostremoveguest.md) functions. Code Signing Services uses this information to report hosting status to callers directly without consulting the host. A code host running in proxy hosting mode cannot switch to dynamic hosting mode.

## Parameters

- `host`: A guest code object identifying the code that is to be the direct host of the new guest. Pass [`kSecNoGuest`](./ksecnoguest.md) if the process calling this function is to be the host. To create a guest of another guest (extending the hosting chain), pass the guest code object of the guest that is to act as the new guest’s host. If the specified host already has a dedicated guest, then that dedicated guest becomes the actual host of the new guest (unless the dedicated guest also has a dedicated guest, in which case the same algorithm is replied recursively). See [`kSecCSDedicatedHost`](./kseccsdedicatedhost.md) for a discussion of dedicated hosts.
- `status`: Code status flags for the new guest (see [`SecCodeStatus`](./seccodestatus.md)). Note that certain code status flags can be set only once, by the caller of the [`SecHostCreateGuest`](./sechostcreateguest.md) function when it creates the guest. In particular, if you do not set the [`valid`](./seccodestatus/valid.md) flag during creation of the guest, then the new guest is created dynamically invalid and can never become dynamically valid.
- `path`: The canonical path to the guest’s code on disk. This is the path you would pass to the [`SecStaticCodeCreateWithPath(_:_:_:)`](./secstaticcodecreatewithpath%28_,_,_%29.md) function to make a static code object reference. You must use an absolute path.
- `attributes`: A key-value dictionary of attributes that can be used to identify this particular guest among all of the caller’s guests. The [`kSecGuestAttributeCanonical`](./ksecguestattributecanonical.md) attribute—containing the guest’s code object (that is, the [`SecGuestRef`](./secguestref.md) object returned in the `newGuest` parameter) is automatically added to the guest’s attributes. Pass `NULL` for this parameter if you do not want to establish any other attributes for this guest. Although you can specify any key-value pairs in this attributes dictionary, the keys in [Guest Attribute Dictionary Keys](./guest-attribute-dictionary-keys.md) are conventionally used for this purpose.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) and [Guest Creation Flags](./guest-creation-flags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior. Pass [`kSecCSDedicatedHost`](./kseccsdedicatedhost.md) to make the code specified in the `host` parameter the dedicated host for the new guest.
- `newGuest`: On return, the guest code object that identifies the new guest.

## See Also

### Related Documentation
- [SecHostSelectGuest](./sechostselectguest.md)
  Makes the calling thread the proxy for a specified guest.
- [SecHostSetHostingPort](./sechostsethostingport.md)
  Tells code signing services that the calling code will directly respond to hosting inquiries over the given port.
- [SecHostRemoveGuest](./sechostremoveguest.md)
  Removes a guest from a host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sechostcreateguest)*