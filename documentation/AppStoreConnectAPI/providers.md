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
- [List All Source Code Management Providers](get-v1-scmproviders.md)
  List all source code management providers you connected to Xcode Cloud.
- [Get a Source Code Management Provider](get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [List all Repositories for a Source Code Management Provider](get-v1-scmproviders-_id_-repositories.md)
  List all Git repositories for a specific source code management provider you connected to Xcode Cloud.
- [GET /v1/scmProviders/{id}/relationships/repositories](get-v1-scmproviders-_id_-relationships-repositories.md)
### Objects
- [object ScmProvider](scmprovider.md)
  The data structure that represents a Providers resource.
- [object ScmProviderResponse](scmproviderresponse.md)
  A response that contains a single Providers resource.
- [object ScmProvidersResponse](scmprovidersresponse.md)
  A response that contains a list of Providers resources.
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