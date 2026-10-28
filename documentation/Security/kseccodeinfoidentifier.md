# kSecCodeInfoIdentifier

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is the signing identifier sealed into the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoIdentifier: CFString
```

```c
extern CFStringRef const kSecCodeInfoIdentifier;
```

## Discussion

The value is a [`CFString`](../CoreFoundation/cfstring.md) object. Absent for unsigned code.

This is generic information returned regardless of which [Code Signing Information Flags](./code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoidentifier)*