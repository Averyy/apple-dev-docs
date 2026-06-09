# SystemMigration.CustomBehaviorItem.PathsItem

**Framework**: Device Management  
**Kind**: dictionary

The custom behavior path dictionary.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
object SystemMigration.CustomBehaviorItem.PathsItem
```

## Properties

- `SourcePath` (string) *(required)*: The path to the migrating file or directory on the source system.
- `SourcePathInUserHome` (boolean) *(required)*: If `true`, the source path is located within a user home directory.
- `TargetPath` (string) *(required)*: The path to the destination file or directory on the target system.
- `TargetPathInUserHome` (boolean) *(required)*: If `true`, the target path is located within a user home directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemmigration/custombehavioritem/pathsitem)*