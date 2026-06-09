# Providers

**Framework**: App Store Connect API

Read information about source code management providers you connected to Xcode Cloud.

#### Overview

The `scmProviders` resource represents the source code management (SCM) providers you connected to Xcode Cloud. Use it to access these SCM providers and read the following information for each provider:

- A unique identifier
- The provider’s type
- The provider’s URL

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Provider Information
- [List all source code management providers](get-v1-scmproviders.md)
  List all source code management providers you connected to Xcode Cloud.
- [Get a source code management provider](get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [List all repositories for a source code management provider](get-v1-scmproviders-_id_-repositories.md)
  List all Git repositories for a specific source code management provider you connected to Xcode Cloud.
- [List repository IDs for an SCM provider](get-v1-scmproviders-_id_-relationships-repositories.md)
### Objects
- [object ScmProvider](scmprovider.md)
  A source code management provider, such as GitHub or Bitbucket, connected to Xcode Cloud for accessing repositories.
- [object ScmProviderResponse](scmproviderresponse.md)
  The response body for endpoints that read a single SCM provider connected to Xcode Cloud.
- [object ScmProvidersResponse](scmprovidersresponse.md)
  The response body for endpoints that list SCM providers connected to Xcode Cloud.
- [object ScmProviderRepositoriesLinkagesResponse](scmproviderrepositorieslinkagesresponse.md)

## See Also

- [Repositories](repositories.md)
  Read detailed information for each repository Xcode Cloud can access, including Git references and pull requests.
- [Pull Requests](pull-requests.md)
  Read pull request information such as source and destination branches.
- [Git References](git-references.md)
  Read information about the canonical reference for a Git branch or tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/providers)*