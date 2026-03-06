# CiBuildAction.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe a Build Actions resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildAction.Attributes
```

## Topics

### Types
- [type CiActionType](ciactiontype.md)
  A string that represents the type of an Xcode Cloud workflow’s action.

## Properties

- `actionType` (CiActionType): The type of the build action.
- `completionStatus` (CiCompletionStatus): The status of the action.
- `executionProgress` (CiExecutionProgress): A string that indicates the progress of the build action.
- `finishedDate` (date-time): The date and time when Xcode Cloud finished performing the action.
- `isRequiredToPass` (boolean): A Boolean value that indicates whether the action must succeed in order for a build to succeed.
- `issueCounts` (CiIssueCounts): An integer value that represents the number of issues Xcode Cloud encountered when it performed the action.
- `name` (string): The name of the build action; for example, `Archive iOS`.
- `startedDate` (date-time): The date and time when Xcode Cloud started performing the action.

## See Also

- [object CiBuildAction.Relationships](cibuildaction/relationships-data.dictionary.md)
  The relationships of the Build Actions resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildaction/attributes-data.dictionary)*