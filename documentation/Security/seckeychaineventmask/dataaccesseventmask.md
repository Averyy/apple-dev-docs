# dataAccessEventMask

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

If the bit specified by this mask is set, your callback function is invoked when a process accesses a keychain item’s data.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.15

> **Deprecated**: Read events are no longer posted

## Declaration

```swift
static var dataAccessEventMask: SecKeychainEventMask { get }
```

```c
kSecDataAccessEventMask
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaineventmask/dataaccesseventmask)*