# SecKeychainEventMask

**Framework**: Security  
**Kind**: struct

Bit masks corresponding to the events that can trigger a keychain callback.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecKeychainEventMask
```

#### Overview

Bitwise `OR` one or more of these masks together to provide the `eventMask` input to the [`SecKeychainAddCallback(_:_:_:)`](seckeychainaddcallback(_:_:_:).md) function to indicate what event or events should trigger your callback.

## Topics

### Initializers
- [init(rawValue: UInt32)](seckeychaineventmask/init(rawvalue:).md)
  Initializes an event mask value.
### Constants
- [static var lockEventMask: SecKeychainEventMask](seckeychaineventmask/lockeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a keychain is locked.
- [static var unlockEventMask: SecKeychainEventMask](seckeychaineventmask/unlockeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a keychain is unlocked.
- [static var addEventMask: SecKeychainEventMask](seckeychaineventmask/addeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when an item is added to a keychain.
- [static var deleteEventMask: SecKeychainEventMask](seckeychaineventmask/deleteeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when an item is deleted from a keychain.
- [static var updateEventMask: SecKeychainEventMask](seckeychaineventmask/updateeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a keychain item is updated.
- [static var passwordChangedEventMask: SecKeychainEventMask](seckeychaineventmask/passwordchangedeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when the keychain password is changed.
- [static var defaultChangedEventMask: SecKeychainEventMask](seckeychaineventmask/defaultchangedeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a different keychain is specified as the default.
- [static var dataAccessEventMask: SecKeychainEventMask](seckeychaineventmask/dataaccesseventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a process accesses a keychain item’s data.
- [static var keychainListChangedMask: SecKeychainEventMask](seckeychaineventmask/keychainlistchangedmask.md)
  If the bit specified by this mask is set, your callback function is invoked when a keychain list is changed.
- [static var trustSettingsChangedEventMask: SecKeychainEventMask](seckeychaineventmask/trustsettingschangedeventmask.md)
  If the bit specified by this mask is set, your callback function is invoked when there is a change in certificate trust settings.
- [static var everyEventMask: SecKeychainEventMask](seckeychaineventmask/everyeventmask.md)
  If all the bits are set, your callback function is invoked whenever any event occurs.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaineventmask)*