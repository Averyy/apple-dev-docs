# SecTrustSettingsSetTrustSettings(_:_:_:)

**Framework**: Security  
**Kind**: func

Specifies trust settings for a certificate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTrustSettingsSetTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettingsDictOrArray: CFTypeRef?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If you pass `NULL` for the `trustSettingsDictOrArray` parameter, then the trust settings for this certificate are stored as an empty trust settings array, indicating “always trust this root certificate regardless of use.” This setting is valid only for a self-signed (root) certificate. To instead remove all trust settings for the certificate (interpreted as “this certificate must be verified to a known trusted certificate”), use the [`SecTrustSettingsRemoveTrustSettings(_:_:)`](sectrustsettingsremovetrustsettings(_:_:).md) function.

If the specified certificate already has trust settings in the specified domain, this function replaces them.

##### Special Considerations

When making changes to per-user trust settings, the user is prompted with an alert panel asking for authentication (user name and password or other credentials normally used for login). Therefore, it is not possible to modify per-user trust settings when not running in a GUI environment (that is, when the user is not logged in via the login window). When making changes to system-wide trust settings, the user is prompted with an alert panel asking for an administrator’s name and password unless the calling process is running as root, in which case no further authentication is needed. Note that this function might block while waiting for user input.

## Parameters

- `certRef`: The certificate for which you want to specify the trust settings. Pass the value   to set the default root certificate trust settings for the domain.
- `domain`: The trust settings domain of the trust settings that you wish to specify.  For possible values, see  .
- `trustSettingsDictOrArray`: The trust settings you wish to specify for this certificate, in the form of a   object, a   of   objects, or  . The contents of   objects used to specify trust settings are detailed in the   function description. Pass   if you want to specify an empty trust settings array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingssettrustsettings(_:_:_:))*