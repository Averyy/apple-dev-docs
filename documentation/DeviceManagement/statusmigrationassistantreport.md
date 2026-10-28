# StatusMigrationAssistantReport

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The status item that reports the state of a completed migration.

**Availability**:
- macOS 26.4+

## Declaration

```
object StatusMigrationAssistantReport
```

## Discussion

### Status item availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

### Status item example

```json
{
    "migration-assistant": {
        "report": {
            "completed-data-size": 53687091200,
            "completed-file-count": 125000,
            "completion-time": "2025-05-15T14:30:00Z",
            "source-user": "user",
            "start-time": "2025-05-15T12:00:00Z",
            "target-user": "user",
            "total-data-size": 53687091200,
            "total-file-count": 125000
        }
    }
}
```

## Topics

### Objects
- [object StatusMigrationAssistantReportMigrationAssistantReportObject](./statusmigrationassistantreportmigrationassistantreportobject.md)
  The Migration Assistant migration status.

## Properties

- `migration-assistant.report` (StatusMigrationAssistantReportMigrationAssistantReportObject) *(required)*: The Migration Assistant migration status.

## See Also

### Migration assisstant items
- [object StatusMigrationAssistantState](./statusmigrationassistantstate.md)
  A status item that shows the device’s current migration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmigrationassistantreport)*