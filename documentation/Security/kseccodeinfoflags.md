# kSecCodeInfoFlags

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the static (on-disk) state of the object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoFlags: CFString
```

```c
extern CFStringRef const kSecCodeInfoFlags;
```

## Discussion

The value is a [`CFNumber`](../CoreFoundation/cfnumber.md). See [`SecCodeSignatureFlags`](./seccodesignatureflags.md) for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoflags)*