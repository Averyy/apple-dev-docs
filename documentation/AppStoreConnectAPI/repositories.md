# Repositories

**Framework**: App Store Connect API

Read detailed information for each repository Xcode Cloud can access, including Git references and pull requests.

#### Overview

The `scmRepositories` resource represents Git repositories Xcode Cloud can access. Use it to retrieve all repositories for a source code management provider you connected to Xcode Cloud and read:

- The name and owner of the repository
- The date when Xcode Cloud last accessed the repository
- The HTTP and SSH URLs for cloning the repository

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

 This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Repository Information
- [List All Git Repositories](get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [Read Git Repository Information](get-v1-scmrepositories-_id_.md)
  Get information about a Git repository that Xcode Cloud can access.
- [List All Git References for a Repository](get-v1-scmrepositories-_id_-gitreferences.md)
  List all Git references for a specific repository that Xcode Cloud can access.
- [List All Pull Requests for a Repository](get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
### Objects
- [object ScmRepository](scmrepository.md)
  The data structure that represents a Repositories resource.
- [object ScmRepositoryResponse](scmrepositoryresponse.md)
  A response that contains a single Repositories resource.
- [object ScmRepositoriesResponse](scmrepositoriesresponse.md)
  A response that contains a list of Repositories resources.

## See Also

- [Providers](providers.md)
  Read information about source code management providers you connected to Xcode Cloud.
- [Pull Requests](pull-requests.md)
  Read pull request information such as source and destination branches.
- [Git References](git-references.md)
  Read information about the canonical reference for a Git branch or tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/repositories)*