# userInfo

**Framework**: Core Data  
**Kind**: property

The user info for the migration manager.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

#### Discussion

You can use the user info dictionary to aid the customization of your migration process.

## See Also

- [var usesStoreSpecificMigrationManager: Bool](nsmigrationmanager/usesstorespecificmigrationmanager.md)
  A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/userinfo)*