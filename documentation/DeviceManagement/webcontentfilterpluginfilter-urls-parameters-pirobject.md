# WebContentFilterPluginFilter_URLs_Parameters_PIRObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary containing Private Information Retrieval server settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
object WebContentFilterPluginFilter_URLs_Parameters_PIRObject
```

## Properties

- `AuthenticationTokenAssetReference` (string): The identifier of an asset declaration containing the HTTP bearer token required to authenticate with the service. The bearer token is provided in the `Password` field of the asset data. The system uses this token to attest that it’s a valid user when requesting anonymous authentication tokens for PIR exchanges.
- `PrivacyPassIssuerURL` (string) *(required)*: The URL containing the domain name of Privacy Pass Issuer.
- `ServerURL` (string) *(required)*: The URL containing the domain name of the private information retrieval server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilterpluginfilter_urls_parameters_pirobject)*