# CiArtifact

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents the output of an Xcode Cloud build action resource.

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
  A response that contains a single Artifacts resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciartifact)*