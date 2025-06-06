# kSecCodeInfoPList

**Framework**: Security  
**Kind**: var

A key whose value is an information dictionary containing the contents of the secured `Info.plist` file as seen by Code Signing Services.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoPList: CFString
```

#### Discussion

The value is a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) object. Absent if no information property list (`Info.plist`) file is known to Code Signing Services. Note that this is not necessarily the same dictionary as the one that would be returned by a [`CFBundle`](https://developer.apple.com/documentation/CoreFoundation/CFBundle) function such as [`CFBundleCopyInfoDictionaryForURL(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFBundleCopyInfoDictionaryForURL(_:)), because [`CFBundle`](https://developer.apple.com/documentation/CoreFoundation/CFBundle) is free to add entries to the information property list).

This is generic information returned regardless of which [`Code Signing Information Flags`](code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoplist)*