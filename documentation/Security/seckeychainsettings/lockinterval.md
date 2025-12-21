# lockInterval

**Framework**: Security  
**Kind**: property

The number of seconds to wait before the keychain locks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var lockInterval: UInt32
```

#### Discussion

If you set [`useLockInterval`](seckeychainsettings/uselockinterval.md) to [`false`](https://developer.apple.com/documentation/Swift/false), set [`lockInterval`](seckeychainsettings/lockinterval.md) to `INT_MAX` to indicate that the keychain never locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsettings/lockinterval)*