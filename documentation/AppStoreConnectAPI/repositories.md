# Repositories

**Framework**: App Store Connect API

Read detailed information for each repository Xcode Cloud can access, including Git references and pull requests.

#### Overview

The `scmRepositories` resource represents Git repositories Xcode Cloud can access. Use it to retrieve all repositories for a source code management provider you connected to Xcode Cloud and read:

- The name and owner of the repository
- The date when Xcode Cloud last accessed the repository
- The HTTP and SSH URLs for cloning the repository

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Repository Information
- [List all git repositories](get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [Read git repository information](get-v1-scmrepositories-_id_.md)
  Get information about a Git repository that Xcode Cloud can access.
- [List all git references for a repository](get-v1-scmrepositories-_id_-gitreferences.md)
  List all Git references for a specific repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-pullrequests.md)
### Objects
- [object ScmRepository](scmrepository.md)
  A source code repository connected to Xcode Cloud, used as the source for workflow builds.
- [object ScmRepositoryResponse](scmrepositoryresponse.md)
  The response body for endpoints that read a single SCM repository connected to Xcode Cloud.
- [object ScmRepositoriesResponse](scmrepositoriesresponse.md)
  The response body for endpoints that list SCM repositories connected to Xcode Cloud.
- [object ScmRepositoryGitReferencesLinkagesResponse](scmrepositorygitreferenceslinkagesresponse.md)
- [object ScmRepositoryPullRequestsLinkagesResponse](scmrepositorypullrequestslinkagesresponse.md)

## See Also

- [Providers](providers.md)
  Read information about source code management providers you connected to Xcode Cloud.
- [Pull Requests](pull-requests.md)
  Read pull request information such as source and destination branches.
- [Git References](git-references.md)
  Read information about the canonical reference for a Git branch or tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/repositories)*