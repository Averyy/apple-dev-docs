# kSecCodeInfoFormat

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a string representing the type and format of the code in a form suitable for display to a knowledgeable user.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoFormat: CFString
```

```c
extern CFStringRef const kSecCodeInfoFormat;
```

## Discussion

The value is a [`CFString`](../CoreFoundation/cfstring.md) object.

This is generic information returned regardless of which [Code Signing Information Flags](./code-signing-information-flags.md)  you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoformat)*