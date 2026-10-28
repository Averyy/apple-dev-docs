# initWithMigrationStages:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Creates a migration manager with the specified stages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithMigrationStages:(NSArray<__kindof NSMigrationStage *> *) stages;
```

## Return Value

An initialized migration manager, or `nil` if Core Data can’t create one.

## Discussion

> ❗ **Important**:  Core Data processes the migration stages in the order that you provide them.

## Parameters

- `stages`: The array of migration stages to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager/initwithmigrationstages:)*