# currentEntityMapping

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity mapping currently being processed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentEntityMapping: NSEntityMapping { get }
```

```objc
@property (strong, readonly) NSEntityMapping * currentEntityMapping;
```

#### Discussion

Each entity is processed a total of three times—instance creation, relationship creation, and validation.

##### Special Considerations

You can observe this value using key-value observing.

## See Also

### Monitoring a Migration’s Progress
- [var migrationProgress: Float](./migrationprogress.md)
  A number between `0` and `1` that indicates the proportion of completeness of the migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/currententitymapping)*