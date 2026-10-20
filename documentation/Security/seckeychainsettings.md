# SecKeychainSettings

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A structure that contains information about keychain settings.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecKeychainSettings
```

```c
struct SecKeychainSettings;
```

#### Overview

This structure contains information about a keychain’s settings such as locking on sleep and the lock time interval. Use the [`SecKeychainSetSettings(_:_:)`](./seckeychainsetsettings%28_,_%29.md) and [`SecKeychainCopySettings(_:_:)`](./seckeychaincopysettings%28_,_%29.md) functions to set and copy a keychain’s settings.

## Topics

### Initializers
- [init()](./seckeychainsettings/init%28%29.md)
  Initializes a keychain settings structure with default values.
- [init(version: UInt32, lockOnSleep: DarwinBoolean, useLockInterval: DarwinBoolean, lockInterval: UInt32)](./seckeychainsettings/init%28version,lockonsleep,uselockinterval,lockinterval%29.md)
  Initializes a keychain settings structures with the given values.
### Instance Properties
- [var lockInterval: UInt32](./seckeychainsettings/lockinterval.md)
  The number of seconds to wait before the keychain locks.
- [var lockOnSleep: DarwinBoolean](./seckeychainsettings/lockonsleep.md)
  A Boolean value indicating whether the keychain locks when the system sleeps.
- [var useLockInterval: DarwinBoolean](./seckeychainsettings/uselockinterval.md)
  A Boolean value indicating whether the keychain automatically locks after a certain period of time.
- [var version: UInt32](./seckeychainsettings/version.md)
  The keychain version.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsettings)*