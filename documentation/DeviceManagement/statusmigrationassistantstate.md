# StatusMigrationAssistantState

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A status item that shows the device’s current migration state.

**Availability**:
- macOS 26.4+

## Declaration

```
object StatusMigrationAssistantState
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
        "state": "completed"
    }
}
```

## Properties

- `migration-assistant.state` (string) *(required)*: The current migration state of the system, which has the following possible values:

  - `none`: Migration hasn’t started yet or no migration has taken place.
  - `migrating`: Migration is in progress.
  - `completed`: Migration has completed successfully.
  - `failed`: Migration has failed.
  - `cancelled`: The user cancelled migration.
  - `unknown`: Migration status is unknown.

  **Allowed Values**: `waiting`, `migrating`, `completed`, `failed`, `cancelled`, `unknown`

## See Also

### Migration assisstant items
- [object StatusMigrationAssistantReport](./statusmigrationassistantreport.md)
  The status item that reports the state of a completed migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmigrationassistantstate)*