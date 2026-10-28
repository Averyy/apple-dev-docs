# usesStoreSpecificMigrationManager

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var usesStoreSpecificMigrationManager: Bool { get set }
```

```objc
@property BOOL usesStoreSpecificMigrationManager;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver uses a store-specific migration manager, otherwise [`false`](../../Swift/false.md).

## Discussion

[`true`](../../Swift/true.md) if the receiver uses a store-specific migration manager, otherwise [`false`](../../Swift/false.md). The default value is [`true`](../../Swift/true.md).

A store-specific migration manager class is not guaranteed to perform any of the migration manager delegate callbacks or update values for the observable properties.

## See Also

### Customizing the Manager
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info for the migration manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/usesstorespecificmigrationmanager)*