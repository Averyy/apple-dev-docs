# CiBuildRun.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe a Build Runs resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildRun.Attributes
```

## Topics

### Objects and types
- [object CiBuildRun.Attributes.DestinationCommit](cibuildrun/attributes-data.dictionary/destinationcommit-data.dictionary.md)
  The latest commit of a pull request’s target branch or the source commit for builds that aren’t pull request builds.
- [object CiBuildRun.Attributes.SourceCommit](cibuildrun/attributes-data.dictionary/sourcecommit-data.dictionary.md)
  The latest commit of a Git branch or tag, or of a pull request’s source branch.
- [object CiGitUser](cigituser.md)
  The Git identity (name and email) of the person who authored or committed the code change that triggered an Xcode Cloud build.
- [object CiIssueCounts](ciissuecounts.md)
  A summary of the warnings, errors, analyzer warnings, and test failures in an Xcode Cloud build run.
- [type CiCompletionStatus](cicompletionstatus.md)
  A string that represents the completion status of an Xcode Cloud build.
- [type CiExecutionProgress](ciexecutionprogress.md)
  A string that represents the progress of an ongoing Xcode Cloud build.

## Properties

- `cancelReason` (string): A string that indicates the reason for a canceled build.
- `completionStatus` (CiCompletionStatus): A string that indicates the status of a completed build.
- `createdDate` (date-time): The date and time when Xcode Cloud created the build.
- `destinationCommit` (CiBuildRun.Attributes.DestinationCommit): Detailed information about the commit of a pull request build’s target branch. This value is only available to builds from pull requests.
- `executionProgress` (CiExecutionProgress): A string that indicates the progress of the build action.
- `finishedDate` (date-time): The date and time when Xcode Cloud completed the build.
- `isPullRequestBuild` (boolean): A Boolean value that indicates whether the build was started by a change to a pull request.
- `issueCounts` (CiIssueCounts): An integer value that represents the number of issues Xcode Cloud encountered when it performed the build.
- `number` (integer): The Xcode Cloud build number.
- `sourceCommit` (CiBuildRun.Attributes.SourceCommit): Detailed information about the commit of a pull request build’s source branch. This value is only available to builds from pull requests.
- `startedDate` (date-time): The date and time when Xcode Cloud started the build.
- `startReason` (string): A string that indicates what started the build.

## See Also

- [object CiBuildRun.Relationships](cibuildrun/relationships-data.dictionary.md)
  The relationships of the Build Runs resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/attributes-data.dictionary)*