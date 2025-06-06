# kSecCodeInfoMainExecutable

**Framework**: Security  
**Kind**: var

A key whose value is a URL locating the main executable file of the code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoMainExecutable: CFString
```

#### Discussion

The value is a [`CFURL`](https://developer.apple.com/documentation/CoreFoundation/CFURL) object. For single files, the URL locates the file itself. For bundles, it locates the main executable as identified by the bundle’s `Info.plist` file.

This is generic information returned regardless of which [`Code Signing Information Flags`](code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfomainexecutable)*