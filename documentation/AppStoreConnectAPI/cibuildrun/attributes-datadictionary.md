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

### Objects and Types
- [object CiBuildRun.Attributes.DestinationCommit](cibuildrun/attributes-data.dictionary/destinationcommit-data.dictionary.md)
  The latest commit of a pull request’s target branch or the source commit for builds that aren’t pull request builds.
- [object CiBuildRun.Attributes.SourceCommit](cibuildrun/attributes-data.dictionary/sourcecommit-data.dictionary.md)
  The latest commit of a Git branch or tag, or of a pull request’s source branch.
- [object CiGitUser](cigituser.md)
  The data structure that represents a Git Users resource.
- [object CiIssueCounts](ciissuecounts.md)
  The data structure that represents an Issue Counts resource.
- [type CiCompletionStatus](cicompletionstatus.md)
  A string that represents the completion status of an Xcode Cloud build.
- [type CiExecutionProgress](ciexecutionprogress.md)
  A string that represents the progress of an ongoing Xcode Cloud build.

## See Also

- [object CiBuildRun.Relationships](cibuildrun/relationships-data.dictionary.md)
  The relationships of the Build Runs resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/attributes-data.dictionary)*