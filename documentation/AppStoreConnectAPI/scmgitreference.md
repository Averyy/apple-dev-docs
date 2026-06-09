# ScmGitReference

**Framework**: App Store Connect API  
**Kind**: dictionary

A Git branch, tag, or commit reference in a source code repository connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmGitReference
```

## Topics

### Objects and types
- [object ScmGitReference.Attributes](scmgitreference/attributes-data.dictionary.md)
  The attributes that describe a Git Reference resource.
- [object ScmGitReference.Relationships](scmgitreference/relationships-data.dictionary.md)
  The relationships of the Git References resource you included in the request and those on which you can operate.
- [type CiGitRefKind](cigitrefkind.md)
  A string that represents the kind of a Git References resource.

## Properties

- `attributes` (ScmGitReference.Attributes): The attributes that describe the Git References resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Git References resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (ScmGitReference.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object ScmGitReferenceResponse](scmgitreferenceresponse.md)
  The response body for endpoints that read a single SCM Git reference in Xcode Cloud.
- [object ScmGitReferencesResponse](scmgitreferencesresponse.md)
  The response body for endpoints that list Git references in an Xcode Cloud repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmgitreference)*