# CKSyncEngine.Event.stateUpdate(_:)

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The sync engine updated its state.

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
case stateUpdate(CKSyncEngine.Event.StateUpdate)
```

#### Discussion

You should persist it locally.

## See Also

### State updates
- [CKSyncEngine.Event.StateUpdate](./stateupdate.md)
  The sync engine state was updated, and you should persist it locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/stateupdate(_:))*