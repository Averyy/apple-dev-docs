# kSecCodeInfoPList

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is an information dictionary containing the contents of the secured `Info.plist` file as seen by Code Signing Services.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoPList: CFString
```

```c
extern CFStringRef const kSecCodeInfoPList;
```

## Discussion

The value is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) object. Absent if no information property list (`Info.plist`) file is known to Code Signing Services. Note that this is not necessarily the same dictionary as the one that would be returned by a [`CFBundle`](../CoreFoundation/cfbundle.md) function such as [`CFBundleCopyInfoDictionaryForURL(_:)`](../CoreFoundation/cfbundlecopyinfodictionaryforurl%28_%29.md), because [`CFBundle`](../CoreFoundation/cfbundle.md) is free to add entries to the information property list).

This is generic information returned regardless of which [Code Signing Information Flags](./code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoplist)*