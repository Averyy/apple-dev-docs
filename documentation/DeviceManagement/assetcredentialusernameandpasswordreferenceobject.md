# AssetCredentialUserNameAndPasswordReferenceObject

**Framework**: Device Management  
**Kind**: dictionary

The external reference for an asset-credential user name and password.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialUserNameAndPasswordReferenceObject
```

## Properties

- `ContentType` (string): The media type that describes the data. If present, the system checks the actual media type of the downloaded data, and an error occurs if the values don’t match.
- `DataURL` (string) *(required)*: The URL to retrieve data, which needs to start with `https://`.
- `Hash-SHA-256` (string): A SHA-256 hash of the data stored at the `DataURL`. Don’t set this value if `Size` is `0` as the client ignores it. However, if present, the system checks the actual hash of the downloaded data, and an error occurs if the values don’t match.
- `Size` (integer): The size of the data. Set the size to `0` if there’s no expectation of a response body. If present, the system checks the actual size of the downloaded data, and an error occurs if the values don’t match.

## See Also

- [object AssetCredentialUserNameAndPasswordAuthenticationObject](assetcredentialusernameandpasswordauthenticationobject.md)
  The server authentication details for an asset-credential user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialusernameandpasswordreferenceobject)*