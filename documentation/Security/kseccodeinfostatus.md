# kSecCodeInfoStatus

**Framework**: Security  
**Kind**: var

A key whose value is the set of code status flags for the running code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoStatus: CFString
```

#### Discussion

The value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object. This is a snapshot taken at the time the function is executed and may be out of date by the time you examine it. Note, however, that some flag values cannot be changed and are therefore permanently reliable. See [`SecCodeStatus`](seccodestatus.md) for a list of possible values.

Specify the [`kSecCSDynamicInformation`](kseccsdynamicinformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfostatus)*