# init(version:lockOnSleep:useLockInterval:lockInterval:)

**Framework**: Security  
**Kind**: init

Initializes a keychain settings structures with the given values.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(version: UInt32, lockOnSleep: DarwinBoolean, useLockInterval: DarwinBoolean, lockInterval: UInt32)
```

## Parameters

- `version`: The keychain version. Use  .
- `lockOnSleep`: A Boolean indicating whether the keychain locks when the system enters sleep mode.
- `useLockInterval`: A Boolean indicating whether the keychain locks after an time period elapses, as given by  .
- `lockInterval`: The number of seconds after which the keychain should lock if   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsettings/init(version:lockonsleep:uselockinterval:lockinterval:))*