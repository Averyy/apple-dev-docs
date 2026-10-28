# kSecCodeInfoSource

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The source of the code signature used for the code object in a format suitable for display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoSource: CFString
```

```c
extern CFStringRef const kSecCodeInfoSource;
```

## Discussion

The value is a [`CFString`](../CoreFoundation/cfstring.md) object. This string is for display purposes only. Don’t rely on the precise value returned.

This is generic information returned regardless of which [Code Signing Information Flags](./code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfosource)*