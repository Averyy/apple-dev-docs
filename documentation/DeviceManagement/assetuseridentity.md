# AssetUserIdentity

**Framework**: Device Management  
**Kind**: dictionary

The user-identity data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetUserIdentity
```

#### Discussion

Specify `com.apple.asset.useridentity` as the declaration type.

##### Asset Example

```json
{
  "Type": "com.apple.asset.useridentity",
  "Identifier": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4",
  "ServerToken": "F25C68F6-D2E5-4A09-9170-F21E8FAD6A2F",
  "Payload": {
    "FullName": "A User",
    "EmailAddress": "a.user@example.com"
  }
}
```

## See Also

- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to a PKCS #1 or PEM encoded certificate.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to a SCEP identity.
- [object AssetCredentialUserNameAndPassword](assetcredentialusernameandpassword.md)
  A reference to data that describes a credential that represents a user name and password.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetuseridentity)*