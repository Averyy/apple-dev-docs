# ScmGitReference.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe a Git Reference resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmGitReference.Attributes
```

## Properties

- `canonicalName` (string): The canonical name of the Git reference.
- `isDeleted` (boolean): A Boolean value that indicates whether the Git reference was deleted.
- `kind` (CiGitRefKind): A value that indicates whether the Git reference is a tag or a branch.
- `name` (string): The name of the Git reference.

## See Also

- [object ScmGitReference.Relationships](scmgitreference/relationships-data.dictionary.md)
  The relationships of the Git References resource you included in the request and those on which you can operate.
- [type CiGitRefKind](cigitrefkind.md)
  A string that represents the kind of a Git References resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmgitreference/attributes-data.dictionary)*