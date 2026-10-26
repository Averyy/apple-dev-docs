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
@property (strong) CKDatabase * database;
```

#### Discussion

Multiple sync engines can run in the same process, each targeting a different database. For example, you may use one sync engine for a person’s private database and another for their shared database.

> ❗ **Important**: When using CloudKit’s production environment, don’t create multiple sync engines that target the same database. You can, however, do this in the development environment to help testing — for example, to simulate multiple devices syncing back and forth.

## See Also

### Managing attributes
- [automaticallySync](./automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [subscriptionID](./subscriptionid.md)
  The subscription identifier for the associated database.
- [stateSerialization](./stateserialization.md)
  The sync engine’s serialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineconfiguration/database)*