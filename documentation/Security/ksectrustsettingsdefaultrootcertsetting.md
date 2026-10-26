# kSecTrustSettingsDefaultRootCertSetting

**Framework**: Security  
**Kind**: macro  
**Role**: Macro

A value indicating the default root certificate trust settings when used as a certificate object in a trust settings API function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kSecTrustSettingsDefaultRootCertSetting
```

#### Discussion

Use this value with the [`SecTrustSettingsSetTrustSettings(_:_:_:)`](./sectrustsettingssettrustsettings%28_,_,_%29.md) function to set the default trust settings for root certificates. When evaluating trust settings for a root certificate in a given domain, if no matching explicit trust settings exist for that certificate, then the default value for the effective trust setting is returned (assuming that a default has been set and that the result is not [`SecTrustSettingsResult.unspecified`](./sectrustsettingsresult/unspecified.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingsdefaultrootcertsetting)*