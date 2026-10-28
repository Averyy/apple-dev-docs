# SecCertificateCopyPreference

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the preferred certificate for the specified name and key use.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecCertificateCopyPreference(CFStringRef name, uint32 keyUsage, SecCertificateRef*certificate);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

This function is typically used to obtain the preferred encryption certificate for an email recipient.

### Special Considerations

Use [`SecCertificateCopyPreferred(_:_:)`](./seccertificatecopypreferred%28_,_%29.md) for new development instead.

## Parameters

- `name`: A string containing an email address (RFC822) or other name for which a preferred certificate is requested.
- `keyUsage`: A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` to ignore this parameter.
- `certificate`: On return, a reference to the preferred certificate, or `NULL` if none was found. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopypreference)*