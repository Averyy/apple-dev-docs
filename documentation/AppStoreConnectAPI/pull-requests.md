# Pull Requests

**Framework**: App Store Connect API

Read pull request information such as source and destination branches.

#### Overview

The `scmPullRequests` resource represents pull requests (PRs) for repositories Xcode Cloud can access. Use it to access:

- A PR’s number, URL, title, and status
- The destination and source branches
- A value that indicates whether the PR involves more than one repository

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Pull Request Information
- [Read pull request information](get-v1-scmpullrequests-_id_.md)
  Get information about a specific pull request.
### Objects
- [object ScmPullRequest](scmpullrequest.md)
  A pull request in a source code repository connected to Xcode Cloud, which can automatically trigger workflow builds.
- [object ScmPullRequestResponse](scmpullrequestresponse.md)
  The response body for endpoints that read a single SCM pull request linked to Xcode Cloud.
- [object ScmPullRequestsResponse](scmpullrequestsresponse.md)
  The response body for endpoints that list SCM pull requests linked to Xcode Cloud.

## See Also

- [Providers](providers.md)
  Read information about source code management providers you connected to Xcode Cloud.
- [Repositories](repositories.md)
  Read detailed information for each repository Xcode Cloud can access, including Git references and pull requests.
- [Git References](git-references.md)
  Read information about the canonical reference for a Git branch or tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/pull-requests)*