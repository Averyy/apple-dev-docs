# moduleAID

**Framework**: SecureElementCredential  
**Kind**: property

The module identifier of the package with which this instance is associated.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let moduleAID: Data
```

#### Discussion

The combination of the package identifier and this identifier indicates what type the associated applet instance is.

## See Also

- [let instanceAID: Data](credentialsession/credential/instanceinfo/instanceaid.md)
  The unique identifier for the applet instance.
- [let packageAID: Data](credentialsession/credential/instanceinfo/packageaid.md)
  The unique identifier of the package you use to install the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/moduleaid)*