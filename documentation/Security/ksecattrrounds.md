# kSecAttrRounds

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the number of rounds to run the pseudorandom function.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecAttrRounds: CFString
```

```c
extern CFStringRef const kSecAttrRounds;
```

## Discussion

The corresponding value is of type [`CFNumber`](../CoreFoundation/cfnumber.md) and indicates the number of rounds to run the pseudorandom function specified by [`kSecAttrPRF`](./ksecattrprf.md) for a cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrrounds)*