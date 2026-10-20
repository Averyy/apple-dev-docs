# kSecCodeInfoChangedFiles

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a list of all files in the code that may have been modified by the process of signing it.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoChangedFiles: CFString
```

```c
extern CFStringRef const kSecCodeInfoChangedFiles;
```

#### Discussion

The value is a [`CFArray`](../CoreFoundation/cfarray.md) array of [`CFURL`](../CoreFoundation/cfurl.md) objects. Files not in this list have not been touched by the signing operation.

Specify the [`kSecCSContentInformation`](./kseccscontentinformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfochangedfiles)*