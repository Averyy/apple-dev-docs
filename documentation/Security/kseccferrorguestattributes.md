# kSecCFErrorGuestAttributes

**Framework**: Security  
**Kind**: var

A key whose value is a Core Foundation object containing an attribute that is unrecognized or that contains a value of the wrong type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCFErrorGuestAttributes: CFString
```

#### Discussion

This key is present when you pass a bad guest attribute to the [`SecHostCreateGuest`](sechostcreateguest.md) or [`SecHostSetGuestStatus`](sechostsetgueststatus.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccferrorguestattributes)*