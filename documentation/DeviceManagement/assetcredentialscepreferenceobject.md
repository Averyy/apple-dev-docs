# AssetCredentialSCEPReferenceObject

**Framework**: Device Management  
**Kind**: dictionary

The external reference. Ensure that the asset data:

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
object AssetCredentialSCEPReferenceObject
```

#### Discussion

- Is a JSON document that represents the `com.apple.credential.scep` credential type
- Uses a media type of `application/json`, and if it includes a `ContentType` sub-key, that sub-key media type is also `application/json`

## Properties

- `ContentType` (string): The media type that describes the data. If present, the system checks the actual media type of the downloaded data, and an error occurs if the values don’t match.
- `DataURL` (string) *(required)*: The URL to retrieve data, which needs to start with `https://`.
- `Hash-SHA-256` (string): A SHA-256 hash of the data stored at the `DataURL`. Don’t set this value if `Size` is `0` as the client ignores it. However, if present, the system checks the actual hash of the downloaded data, and an error occurs if the values don’t match.
- `Size` (integer): The size of the data. Set the size to `0` if there’s no expectation of a response body. If present, the system checks the actual size of the downloaded data, and an error occurs if the values don’t match.

## See Also

- [object AssetCredentialSCEPAuthenticationObject](assetcredentialscepauthenticationobject.md)
  The server authentication details. If this key is absent, the default authentication type is MDM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assetcredentialscepreferenceobject)*