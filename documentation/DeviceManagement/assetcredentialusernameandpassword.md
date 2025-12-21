# AssetCredentialUserNameAndPassword

**Framework**: Device Management  
**Kind**: dictionary

A reference to data that describes a credential that represents a user name and password.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialUserNameAndPassword
```

#### Discussion

Specify `com.apple.asset.credential.userpassword` as the declaration type.

##### Asset Example

```json
{
    "Type": "com.apple.asset.credential.userpassword",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Reference": {
            "DataURL": "https://example.com/asset-data/credential.json",
            "ContentType": "application/json"
        }
    }
}
```

## Topics

### Objects
- [object AssetCredentialUserNameAndPasswordAuthenticationObject](assetcredentialusernameandpasswordauthenticationobject.md)
  The server authentication details for an asset-credential user name and password.
- [object AssetCredentialUserNameAndPasswordReferenceObject](assetcredentialusernameandpasswordreferenceobject.md)
  The external reference for an asset-credential user name and password.

## See Also

- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to a PKCS #1 or PEM encoded certificate.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to a SCEP identity.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialusernameandpassword)*