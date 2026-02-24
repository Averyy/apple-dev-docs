# AssetCredentialUserNameAndPasswordAuthenticationObject

**Framework**: Device Management  
**Kind**: dictionary

The server authentication details for an asset-credential user name and password.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object AssetCredentialUserNameAndPasswordAuthenticationObject
```

## Properties

- `Type` (string) *(required)*: The type of authentication, which has these allowed values: - `MDM`: A request that uses MDM semantics, which includes the device-identity certificate, and any user authentication. This is equivalent to an MDM request made to the `CheckInURL` or `ServerURL`. This option is only available through declarative device management.
- `None`: A standard GET request.

## See Also

- [object AssetCredentialUserNameAndPasswordReferenceObject](assetcredentialusernameandpasswordreferenceobject.md)
  The external reference for an asset-credential user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialusernameandpasswordauthenticationobject)*