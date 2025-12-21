# AssetData

**Framework**: Device Management  
**Kind**: dictionary

A reference to arbitrary data with a specific media type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetData
```

#### Discussion

Specify `com.apple.asset.data` as the declaration type.

##### Asset Example

```json
{
    "Type": "com.apple.asset.data",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Reference": {
            "DataURL": "https://example.com/asset-data/data/test.txt",
            "ContentType": "text/plain"
        },
        "Authentication": {
            "Type": "MDM"
        }
    }
}
```

## Topics

### Objects
- [object AssetDataAuthenticationObject](assetdataauthenticationobject.md)
  The server authentication details for an asset data.
- [object AssetDataReferenceObject](assetdatareferenceobject.md)
  The external reference for an asset data.

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
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetdata)*