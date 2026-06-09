# CiArtifact

**Framework**: App Store Connect API  
**Kind**: dictionary

A file output produced by an Xcode Cloud build action, such as an app archive, test result bundle, or build log.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiArtifact
```

## Topics

### Objects
- [object CiArtifact.Attributes](ciartifact/attributes-data.dictionary.md)
  The attributes that describe the output of an artifact resource.

## Properties

- `attributes` (CiArtifact.Attributes): The attributes that describe the Artifacts resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an Artifacts resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiArtifactResponse](ciartifactresponse.md)
  The response body for endpoints that read a single artifact produced by an Xcode Cloud build action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciartifact)*