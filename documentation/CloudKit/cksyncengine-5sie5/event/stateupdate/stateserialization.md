# stateSerialization

**Framework**: CloudKit  
**Kind**: property

The current state of the sync engine.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
let stateSerialization: CKSyncEngine.State.Serialization
```

#### Discussion

> ❗ **Important**:  Always persist the most recent state to disk alongside your app data. The sync engine requires you to provide it with the most recent serialized state at initialization, and it’s your responsibility to make sure the state is available across app launches.

 Always persist the most recent state to disk alongside your app data. The sync engine requires you to provide it with the most recent serialized state at initialization, and it’s your responsibility to make sure the state is available across app launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/stateupdate/stateserialization)*