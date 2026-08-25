# AssetCredentialCertificate

**Framework**: Device Management  
**Kind**: dictionary

A reference to one PKCS #1 or PEM encoded certificate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialCertificate
```

#### Discussion

Specify `com.apple.asset.credential.certificate` as the declaration type.

##### Asset Example

```json
{
    "Type": "com.apple.asset.credential.certificate",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Reference": {
            "DataURL": "https://example.com/asset-data/certificates/cert.pem",
            "ContentType": "application/pem"
        }
    }
}
```

## Topics

### Objects
- [object AssetCredentialCertificateAuthenticationObject](assetcredentialcertificateauthenticationobject.md)
  The server authentication details. If this key is absent, the default authentication type is MDM.
- [object AssetCredentialCertificateReferenceObject](assetcredentialcertificatereferenceobject.md)
  The external reference. Ensure the asset data contains exactly one certificate. If the PEM data contains more than one certificate, the system installs the first certificate and ignores the rest. Ensure that the asset data uses a media type of `application/pkcs1` or `application/pem` to correctly identify the type of encoded certificate. If the asset data includes a `ContentType` sub-key, set it to the corresponding media type.

## Properties

- `Authentication` (AssetCredentialCertificateAuthenticationObject): The server authentication details. If this key is absent, the default authentication type is MDM.
- `Reference` (AssetCredentialCertificateReferenceObject) *(required)*: The external reference. Ensure the asset data contains exactly one certificate. If the PEM data contains more than one certificate, the system installs the first certificate and ignores the rest. Ensure that the asset data uses a media type of `application/pkcs1` or `application/pem` to correctly identify the type of encoded certificate. If the asset data includes a `ContentType` sub-key, set it to the corresponding media type.

## See Also

- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to a SCEP identity.
- [object AssetCredentialUserNameAndPassword](assetcredentialusernameandpassword.md)
  A reference to data that describes a credential that represents a user name and password.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialcertificate)*