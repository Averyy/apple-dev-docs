# init(_:)

**Framework**: Core Data  
**Kind**: init

Creates a migration manager with the specified stages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Swift 5.8+

## Declaration

```swift
convenience init(_ stages: [NSMigrationStage])
```

#### Discussion

> ❗ **Important**:  Core Data processes the migration stages in the order that you provide them.

## Parameters

- `stages`: The array of migration stages to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager/init(_:))*