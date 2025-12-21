# appContainer

**Framework**: AppMigrationKit  
**Kind**: property  
**Required**: Yes

The data container of the containing app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var appContainer: MigrationDataContainer { get }
```

#### Discussion

To access the containing app’s data, your app requires the `com.apple.developer.app-migration.data-container-access` entitlement.

## See Also

- [struct MigrationDataContainer](migrationdatacontainer.md)
  An object describing an app’s data container


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationextension/appcontainer)*