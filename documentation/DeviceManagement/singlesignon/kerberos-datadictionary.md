# SingleSignOn.Kerberos

**Framework**: Device Management  
**Kind**: dictionary

The Kerberos dictionary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+

## Declaration

```swift
object SingleSignOn.Kerberos
```

## Properties

- `AppIdentifierMatches` ([string]): The list of app identifiers that the system allows to use this login. If this field missing, the system matches all app identifiers with this login. Don’t set an empty array. The array needs to contain strings that match App Bundle IDs. These strings can be exact matches such as `com.mycompany.myapp`, or they may specify a prefix match on the Bundle ID by using the `\*` wildcard character. The wildcard character needs to appear after a period (`.`), and may only appear once, at the end of the string, for example, `com.mycompany.\*`. When you provide a wildcard, the system grants access to the account to any app with a Bundle ID that begins with the prefix. Deprecated: iOS 26+ | iPadOS 26+
- `PayloadCertificateUUID` (string): The `PayloadUUID` of an identity certificate payload that the system can use to renew the Kerberos credential without user interaction. Set the payload type to either `com.apple.security.pkcs12` or `com.apple.security.scep` in the certificate payload. The configuration file needs to contain both the SSO payload and the identity certificate payload. Available: iOS 8+ | iPadOS 8+
Deprecated: iOS 26+ | iPadOS 26+
- `PrincipalName` (string): The principal name. If not provided, the system prompts the user for one during profile installation. Required for MDM installation. Deprecated: iOS 26+ | iPadOS 26+
- `Realm` (string) *(required)*: The properly capitalized realm name. Deprecated: iOS 26+ | iPadOS 26+
- `URLPrefixMatches` ([string]): The list of URL prefixes to match in order to use this account for Kerberos authentication over HTTP. If this key is missing, the system makes the account eligible to match all `http://` and `https://` URLs. Begin the URL matching patterns with either `http://` or `https://`. The system performs a simple string match, so the URL prefix `http://www.apple.com/` doesn’t match `http://www.apple.com:80/`. However, if a matching pattern doesn’t end in `/`, the system automatically append a `/` to it. Deprecated: iOS 26+ | iPadOS 26+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/singlesignon/kerberos-data.dictionary)*