# instanceAID

**Framework**: SecureElementCredential  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the applet instance.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let instanceAID: Data
```

## Discussion

Use this identifier in [`performWiredTransaction(using:over:instanceAID:)`](../../performwiredtransaction%28using,over,instanceaid%29.md) for UIKit or [`performTransactionInWiredMode(using:instanceAID:)`](../../../credentialtransaction/performtransactioninwiredmode%28using,instanceaid%29.md) for SwiftUI, and when selecting this instance to perform data transceiving.

## See Also

### Inspecting instance identifiers
- [let packageAID: Data](./packageaid.md)
  The unique identifier of the package you use to install the instance.
- [let moduleAID: Data](./moduleaid.md)
  The module identifier of the package with which this instance is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/instanceaid)*