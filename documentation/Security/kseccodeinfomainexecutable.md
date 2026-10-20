# kSecCodeInfoMainExecutable

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a URL locating the main executable file of the code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoMainExecutable: CFString
```

```c
extern CFStringRef const kSecCodeInfoMainExecutable;
```

#### Discussion

The value is a [`CFURL`](../CoreFoundation/cfurl.md) object. For single files, the URL locates the file itself. For bundles, it locates the main executable as identified by the bundle’s `Info.plist` file.

This is generic information returned regardless of which [Code Signing Information Flags](./code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfomainexecutable)*