# DiskManagementSettingsRestrictionsObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The restrictions for the disk.

**Availability**:
- macOS 15.0+

## Declaration

```
object DiskManagementSettingsRestrictionsObject
```

## Properties

- `ExternalStorage` (string): Specifies the mount policy for external storage:

  - `Allowed`: The system can mount external storage that’s read-write or read-only.
  - `ReadOnly`: The system can only mount read-only external storage. Note that external storage that’s read-write won’t be mounted read-only.
  - `Disallowed`: The system can’t mount any external storage.

  **Allowed Values**: `Allowed`, `ReadOnly`, `Disallowed`
- `NetworkStorage` (string): Specifies the mount policy for network storage:

  - `Allowed`: The system can mount network storage that’s read-write or read-only.
  - `ReadOnly`: The system can only mount read-only network storage. Note that network storage that’s read-write won’t be mounted read-only.
  - `Disallowed`: The system can’t mount any network storage.

  **Allowed Values**: `Allowed`, `ReadOnly`, `Disallowed`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/diskmanagementsettingsrestrictionsobject)*