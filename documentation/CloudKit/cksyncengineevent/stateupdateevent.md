# stateUpdateEvent

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The event downcast to the subclass that represents an update to the sync engine’s state.

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
@property (nonatomic, strong, readonly) CKSyncEngineStateUpdateEvent * stateUpdateEvent;
```

## See Also

### Accessing state updates
- [CKSyncEngineStateUpdateEvent](../cksyncenginestateupdateevent.md)
  The sync engine state was updated, and you should persist it locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineevent/stateupdateevent)*