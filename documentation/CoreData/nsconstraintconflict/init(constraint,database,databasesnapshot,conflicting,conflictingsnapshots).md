# init(constraint:database:databaseSnapshot:conflicting:conflictingSnapshots:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes a constraint conflict.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(constraint contraint: [String], database databaseObject: NSManagedObject?, databaseSnapshot: [AnyHashable : Any]?, conflicting conflictingObjects: [NSManagedObject], conflictingSnapshots: [Any])
```

```objc
- (instancetype) initWithConstraint:(NSArray<NSString *> *) contraint databaseObject:(NSManagedObject *) databaseObject databaseSnapshot:(NSDictionary *) databaseSnapshot conflictingObjects:(NSArray<NSManagedObject *> *) conflictingObjects conflictingSnapshots:(NSArray *) conflictingSnapshots;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict/init(constraint:database:databasesnapshot:conflicting:conflictingsnapshots:))*