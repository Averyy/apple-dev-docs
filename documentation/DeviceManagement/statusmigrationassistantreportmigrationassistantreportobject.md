# StatusMigrationAssistantReportMigrationAssistantReportObject

**Framework**: Device Management  
**Kind**: dictionary

The Migration Assistant migration status.

**Availability**:
- macOS 26.4+

## Declaration

```swift
object StatusMigrationAssistantReportMigrationAssistantReportObject
```

## Properties

- `completed-data-size` (integer): The total amount of data the system successfully migrated from the source system.
- `completed-file-count` (integer): The number of files successfully migrated from the source system.
- `completion-time` (string): The RFC 3339 timestamp for when the system completed migration.
- `errors` ([string]): The descriptions of migration errors that the system reports.
- `source-user` (string): The username of the user that the system migrated from the source system.
- `start-time` (string): The RFC 3339 timestamp for when the system started migration.
- `target-user` (string): The username of the target user account on the destination system.
- `total-data-size` (integer): The total amount of data the system considers in scope for migration from the source system.
- `total-file-count` (integer): The number of files the system considers in scope for migration from the source system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmigrationassistantreportmigrationassistantreportobject)*