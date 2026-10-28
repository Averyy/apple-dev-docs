# kSecCodeInfoRequirements

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is the internal requirements of the code as a text string in canonical syntax.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoRequirements: CFString
```

```c
extern CFStringRef const kSecCodeInfoRequirements;
```

## Discussion

The value is a [`CFString`](../CoreFoundation/cfstring.md) object. If there is an explicit designated requirement, then it’s included in this text string.

Specify the [`kSecCSRequirementInformation`](./kseccsrequirementinformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinforequirements)*