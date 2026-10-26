# SecCertificateSetPreference

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the preferred certificate for a specified name, key use, and date.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecCertificateSetPreference(SecCertificateRef certificate, CFStringRef name, uint32 keyUsage, CFDateRef date);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

This function is typically used to set the preferred encryption certificate for an email recipient, either manually (when encrypting email to a recipient) or automatically upon receipt of encrypted email.

##### Special Considerations

Use [`SecCertificateSetPreferred(_:_:_:)`](./seccertificatesetpreferred%28_,_,_%29.md) for new development instead.

Because this preference is stored in the default keychain, if the keychain is locked, the system asks the user for a password or other token to unlock it. This function can therefore block while waiting for user input.

## Parameters

- `certificate`: The certificate object identifying the preferred certificate.
- `name`: A string containing an email address (RFC822) or other name with which the preferred certificate is to be associated.
- `keyUsage`: A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` if you don’t want to specify a particular key use.
- `date`: The date after which this preference is no longer valid. If supplied, the preferred certificate is changed only if this date is later than the currently saved setting. Pass `NULL` if this preference should not be restricted by date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatesetpreference)*