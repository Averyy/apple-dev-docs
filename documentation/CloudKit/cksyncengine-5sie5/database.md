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
- visionOS
- watchOS 10.0+

## Declaration

```swift
final var database: CKDatabase { get }
```

## Discussion

Multiple sync engines can run in the same process, each targeting a different database. For example, you may use one sync engine for a person’s private database and another for their shared database.

## See Also

### Accessing the engine’s attributes
- [var state: CKSyncEngine.State](./state-swift.property.md)
  A collection of state properties used to efficiently manage sync engine operation.
- [CKSyncEngine.State](./state-swift.class.md)
  An object that manages the sync engine’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/database)*