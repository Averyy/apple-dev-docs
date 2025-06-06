# CiBranchStartCondition

**Framework**: App Store Connect API  
**Kind**: dictionary

Settings for a start condition that starts a build if a branch changes.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBranchStartCondition
```

## Topics

### Objects
- [object CiBranchPatterns](cibranchpatterns.md)
  Case-sensitive patterns Xcode Cloud uses to determine if a change meets branch names you configure for a workflow’s start condition.

## See Also

- [object CiTagStartCondition](citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.
- [object CiPullRequestStartCondition](cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiScheduledStartCondition](cischeduledstartcondition.md)
  Settings for a start condition that starts a build based on a schedule.
- [object CiFilesAndFoldersRule](cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibranchstartcondition)*