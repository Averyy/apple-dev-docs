# database

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The associated database.

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
@property (strong, readonly) CKDatabase * database;
```

## Discussion

Multiple sync engines can run in the same process, each targeting a different database. For example, you may use one sync engine for a person’s private database and another for their shared database.

## See Also

### Accessing the engine’s attributes
- [state](./state.md)
  A collection of state properties used to efficiently manage sync engine operation.
- [CKSyncEngineState](../cksyncenginestate.md)
  An object that manages the sync engine’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9/database)*