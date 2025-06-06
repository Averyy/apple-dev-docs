# packageAID

**Framework**: SecureElementCredential  
**Kind**: property

The unique identifier of the package you use to install the instance.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let packageAID: Data
```

#### Discussion

You can use the version encoded in this identifier to determine the version of the installed applet.

## See Also

- [let instanceAID: Data](credentialsession/credential/instanceinfo/instanceaid.md)
  The unique identifier for the applet instance.
- [let moduleAID: Data](credentialsession/credential/instanceinfo/moduleaid.md)
  The module identifier of the package with which this instance is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/packageaid)*