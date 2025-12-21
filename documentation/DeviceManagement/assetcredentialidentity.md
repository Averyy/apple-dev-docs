# AssetCredentialIdentity

**Framework**: Device Management  
**Kind**: dictionary

A reference to a PKCS #12 password-protected identity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialIdentity
```

#### Discussion

Specify `com.apple.asset.credential.identity` as the declaration type.

##### Asset Example

```json
{
    "Type": "com.apple.asset.credential.identity",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Reference": {
            "DataURL": "https://example.com/asset-data/certificates/www.example.com.json",
            "ContentType": "application/json"
        }
    }
}
```

## Topics

### Objects
- [object AssetCredentialIdentityAuthenticationObject](assetcredentialidentityauthenticationobject.md)
  The server authentication details for an asset-credential identity.
- [object AssetCredentialIdentityReferenceObject](assetcredentialidentityreferenceobject.md)
  A dictionary that describes the external reference.

## See Also

- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to a PKCS #1 or PEM encoded certificate.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to a SCEP identity.
- [object AssetCredentialUserNameAndPassword](assetcredentialusernameandpassword.md)
  A reference to data that describes a credential that represents a user name and password.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialidentity)*