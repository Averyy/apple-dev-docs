# CiScheduledStartCondition

**Framework**: App Store Connect API  
**Kind**: dictionary

Settings for a start condition that starts a build based on a schedule.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiScheduledStartCondition
```

## Topics

### Objects
- [object CiScheduledStartCondition.Schedule](cischeduledstartcondition/schedule-data.dictionary.md)
  The schedule of an Xcode Cloud workflow that starts a new build based on a schedule.

## See Also

- [object CiBranchStartCondition](cibranchstartcondition.md)
  Settings for a start condition that starts a build if a branch changes.
- [object CiTagStartCondition](citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.
- [object CiPullRequestStartCondition](cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiFilesAndFoldersRule](cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cischeduledstartcondition)*