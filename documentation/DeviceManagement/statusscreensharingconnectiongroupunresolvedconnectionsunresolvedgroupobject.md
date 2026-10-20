# StatusScreenSharingConnectionGroupUnresolvedConnectionsUnresolvedGroupObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The status item that contains an unresolved connection group.

**Availability**:
- macOS 14.1+

## Declaration

```
object StatusScreenSharingConnectionGroupUnresolvedConnectionsUnresolvedGroupObject
```

## Properties

- `_removed` (boolean): If `true`, the system removed the unresolved connection group and only this key and the `identifier` key are present in the status item object.

  **Default**: `false`
- `identifier` (string) *(required)*: The unique `ConnectionGroupUUID` identifier of the connection group.
- `unresolved_connections` ([string]): An array of `ConnectionUUID` values specified in the `Members` key in the group’s declaration for the unresolved connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusscreensharingconnectiongroupunresolvedconnectionsunresolvedgroupobject)*