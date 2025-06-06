# Git References

**Framework**: Appstoreconnectapi

Read information about the canonical reference for a Git branch or tag.

#### Overview

The `scmGitReferences` resource represents the canonical Git reference for the Git commit that Xcode Cloud used to perform a build. The resource includes the following information:

- The reference’s name and canonical name
- Whether the reference has been deleted
- The type of the reference

For example, if Xcode Cloud uses the `bug-fix` branch for a build, the canonical Git reference is `refs/heads/bug-fix` and the name is `bug-fix`. If Xcode Cloud starts a build for the `release-1.0` tag, the canonical name is `refs/tags/release-1.0` and the name is `release-1.0`.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Information About Git References
- [Read Git Reference Information](get-v1-scmgitreferences-_id_.md)
  Get information about a specific Git reference.
### Objects
- [object ScmGitReference](scmgitreference.md)
  The data structure that represents a Git References resource.
- [object ScmGitReferenceResponse](scmgitreferenceresponse.md)
  A response that contains a single Git References resource.
- [object ScmGitReferencesResponse](scmgitreferencesresponse.md)
  A response that contains a list of Git References resources.

## See Also

- [Providers](providers.md)
  Read information about source code management providers you connected to Xcode Cloud.
- [Repositories](repositories.md)
  Read detailed information for each repository Xcode Cloud can access, including Git references and pull requests.
- [Pull Requests](pull-requests.md)
  Read pull request information such as source and destination branches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/git-references)*