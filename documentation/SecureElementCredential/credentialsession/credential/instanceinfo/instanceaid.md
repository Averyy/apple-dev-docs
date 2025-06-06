# instanceAID

**Framework**: SecureElementCredential  
**Kind**: property

The unique identifier for the applet instance.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let instanceAID: Data
```

#### Discussion

Use this identifier in [`performWiredTransaction(using:over:instanceAID:)`](credentialsession/performwiredtransaction(using:over:instanceaid:).md) for UIKit or [`performTransactionInWiredMode(using:instanceAID:)`](credentialtransaction/performtransactioninwiredmode(using:instanceaid:).md) for SwiftUI, and when selecting this instance to perform data transceiving.

## See Also

- [let packageAID: Data](credentialsession/credential/instanceinfo/packageaid.md)
  The unique identifier of the package you use to install the instance.
- [let moduleAID: Data](credentialsession/credential/instanceinfo/moduleaid.md)
  The module identifier of the package with which this instance is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/instanceaid)*