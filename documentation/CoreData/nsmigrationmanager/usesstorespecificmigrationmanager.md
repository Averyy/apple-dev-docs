# usesStoreSpecificMigrationManager

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var usesStoreSpecificMigrationManager: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver uses a store-specific migration manager, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver uses a store-specific migration manager, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The default value is [`true`](https://developer.apple.com/documentation/swift/true).

A store-specific migration manager class is not guaranteed to perform any of the migration manager delegate callbacks or update values for the observable properties.

## See Also

- [var userInfo: [AnyHashable : Any]?](nsmigrationmanager/userinfo.md)
  The user info for the migration manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/usesstorespecificmigrationmanager)*