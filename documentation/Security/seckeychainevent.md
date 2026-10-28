# SecKeychainEvent

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The list of keychain events that can trigger a callback.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecKeychainEvent
```

```c
enum SecKeychainEvent : UInt32;
```

## Overview

Keychain Services includes one of these events in the callback you register with [`SecKeychainAddCallback(_:_:_:)`](./seckeychainaddcallback%28_,_,_%29.md), using the function signature defined by [`SecKeychainCallback`](./seckeychaincallback.md), to indicate what event triggered the callback.

## Topics

### Constants
- [SecKeychainEvent.lockEvent](./seckeychainevent/lockevent.md)
  Indicates a keychain was locked.
- [SecKeychainEvent.unlockEvent](./seckeychainevent/unlockevent.md)
  Indicates a keychain was successfully unlocked.
- [SecKeychainEvent.addEvent](./seckeychainevent/addevent.md)
  Indicates an item was added to a keychain.
- [SecKeychainEvent.deleteEvent](./seckeychainevent/deleteevent.md)
  Indicates an item was deleted from a keychain.
- [SecKeychainEvent.updateEvent](./seckeychainevent/updateevent.md)
  Indicates a keychain item was updated.
- [SecKeychainEvent.passwordChangedEvent](./seckeychainevent/passwordchangedevent.md)
  Indicates the keychain password was changed.
- [SecKeychainEvent.defaultChangedEvent](./seckeychainevent/defaultchangedevent.md)
  Indicates that a different keychain was specified as the default.
- [SecKeychainEvent.dataAccessEvent](./seckeychainevent/dataaccessevent.md)
  Indicates a process has accessed a keychain item’s data.
- [SecKeychainEvent.keychainListChangedEvent](./seckeychainevent/keychainlistchangedevent.md)
  Indicates the list of keychains has changed.
- [SecKeychainEvent.trustSettingsChangedEvent](./seckeychainevent/trustsettingschangedevent.md)
  Indicates trust settings have changed.
### Initializers
- [init?(rawValue: UInt32)](./seckeychainevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainevent)*