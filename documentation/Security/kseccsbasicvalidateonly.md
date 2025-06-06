# kSecCSBasicValidateOnly

**Framework**: Security  
**Kind**: var

Do not validate either the main executable or the bundle resources, if any.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSBasicValidateOnly: UInt32 { get }
```

#### Discussion

This flag is the bitwise OR of the [`kSecCSDoNotValidateExecutable`](kseccsdonotvalidateexecutable.md) and [`kSecCSDoNotValidateResources`](kseccsdonotvalidateresources.md) flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccsbasicvalidateonly)*