# SystemMigration.CustomBehaviorItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The custom behavior dictionary.

**Availability**:
- macOS 10.12.4+

## Declaration

```
object SystemMigration.CustomBehaviorItem
```

## Topics

### Objects
- [object SystemMigration.CustomBehaviorItem.PathsItem](./custombehavioritem/pathsitem.md)
  The custom behavior path dictionary.

## Properties

- `Context` (string) *(required)*: The context that custom paths apply to.
- `Paths` ([SystemMigration.CustomBehaviorItem.PathsItem]) *(required)*: The list of custom behavior path dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemmigration/custombehavioritem)*