# StatusMigrationAssistantState

**Framework**: Device Management  
**Kind**: dictionary

A status item that shows the device’s current migration state.

**Availability**:
- macOS 26.4+

## Declaration

```swift
object StatusMigrationAssistantState
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "migration-assistant": {
        "state": "completed"
    }
}
```

## Properties

- `migration-assistant.state` (string) *(required)*: The current migration state of the system, which has the following possible values: - `none`: Migration has not started yet or no migration has taken place.
- `migrating`: Migration is in progress.
- `completed`: Migration has completed successfully.
- `failed`: Migration has failed.
- `cancelled`: The user cancelled migration.
- `unknown`: Migration status is unknown.

## See Also

- [object StatusMigrationAssistantReport](statusmigrationassistantreport.md)
  The status item that reports the state of a completed migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmigrationassistantstate)*