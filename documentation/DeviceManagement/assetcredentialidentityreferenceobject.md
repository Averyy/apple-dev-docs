# AssetCredentialIdentityReferenceObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the external reference.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AssetCredentialIdentityReferenceObject
```

#### Discussion

Ensure that the asset data:

- Is a JSON document that represents the `com.apple.credential.identity` credential type
- Uses a media type of `application/json`, and if it includes a `ContentType` sub-key, that sub-key media type is also `application/json`

## See Also

- [object AssetCredentialIdentityAuthenticationObject](assetcredentialidentityauthenticationobject.md)
  The server authentication details for an asset-credential identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialidentityreferenceobject)*