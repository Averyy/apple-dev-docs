# lockInterval

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

The number of seconds to wait before the keychain locks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var lockInterval: UInt32
```

```c
UInt32 lockInterval;
```

## Discussion

If you set [`useLockInterval`](./uselockinterval.md) to [`false`](../../Swift/false.md), set [`lockInterval`](./lockinterval.md) to `INT_MAX` to indicate that the keychain never locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsettings/lockinterval)*