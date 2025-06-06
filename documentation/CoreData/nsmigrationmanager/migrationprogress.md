# migrationProgress

**Framework**: Core Data  
**Kind**: property

A number between `0` and `1` that indicates the proportion of completeness of the migration.

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
var migrationProgress: Float { get }
```

#### Discussion

If a migration is not taking place, this property is `1`. You can observe this value using key-value observing.

## See Also

- [var currentEntityMapping: NSEntityMapping](nsmigrationmanager/currententitymapping.md)
  The entity mapping currently being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/migrationprogress)*