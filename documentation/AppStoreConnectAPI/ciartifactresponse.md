# CiArtifactResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single artifact produced by an Xcode Cloud build action.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiArtifactResponse
```

## Properties

- `data` (CiArtifact) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiArtifact](ciartifact.md)
  A file output produced by an Xcode Cloud build action, such as an app archive, test result bundle, or build log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciartifactresponse)*