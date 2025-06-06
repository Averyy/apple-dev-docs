# kSecCFErrorResourceSeal

**Framework**: Security  
**Kind**: var

A key whose value is a Core Foundation object containing the part of the resource seal that had a problem.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCFErrorResourceSeal: CFString
```

#### Discussion

The `CodeResources` file that gets generated as part of the code signing process serves as the bundle’s seal. This file is a CFDictionary that contains a listing of all the files found within your bundle coupled with their respective hash values and a set of rule definitions. The type of object returned depends on which item in the dictionary had a problem. See [`macOS Code Signing In Depth`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919) for more information on the `CodeResources` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccferrorresourceseal)*