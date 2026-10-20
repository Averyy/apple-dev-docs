# kSecCodeInfoEntitlements

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value represents the embedded entitlement blob of the code, if any.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoEntitlements: CFString
```

```c
extern CFStringRef const kSecCodeInfoEntitlements;
```

#### Discussion

The value is a [`CFData`](../CoreFoundation/cfdata.md) object.

Specify the [`kSecCSRequirementInformation`](./kseccsrequirementinformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoentitlements)*