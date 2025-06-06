# CiWorkflow.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe a Workflows resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflow.Attributes
```

## Topics

### Objects
- [object CiBranchStartCondition](cibranchstartcondition.md)
  Settings for a start condition that starts a build if a branch changes.
- [object CiTagStartCondition](citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.
- [object CiPullRequestStartCondition](cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiScheduledStartCondition](cischeduledstartcondition.md)
  Settings for a start condition that starts a build based on a schedule.
- [object CiFilesAndFoldersRule](cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.

## See Also

- [object CiWorkflow.Relationships](ciworkflow/relationships-data.dictionary.md)
  The relationships of the Workflows resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflow/attributes-data.dictionary)*