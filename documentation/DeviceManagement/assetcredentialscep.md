# AssetCredentialSCEP

**Framework**: Device Management  
**Kind**: dictionary

A reference to a SCEP identity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialSCEP
```

#### Discussion

Specify `com.apple.asset.credential.scep` as the declaration type.

##### Asset Example

```json
{
    "Type": "com.apple.asset.credential.scep",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Reference": {
            "DataURL": "https://example.com/asset-data/certificates/security_scep.json",
            "ContentType": "application/json"
        }
    }
}
```

## Topics

### Objects
- [object AssetCredentialSCEPAuthenticationObject](assetcredentialscepauthenticationobject.md)
  The server authentication details for a SCEP asset credential.
- [object AssetCredentialSCEPReferenceObject](assetcredentialscepreferenceobject.md)
  The external reference for a SCEP asset credential.

## See Also

- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to a PKCS #1 or PEM encoded certificate.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialUserNameAndPassword](assetcredentialusernameandpassword.md)
  A reference to data that describes a credential that represents a user name and password.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialscep)*