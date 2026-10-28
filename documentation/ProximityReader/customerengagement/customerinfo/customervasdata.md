# customerVASData

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The encrypted VAS content of a selected Wallet pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
let customerVASData: Data?
```

## Discussion

The encrypted content of the pass stored in Wallet, which contains the loyalty or reward pass identifier. See [`VASReadResult.ReadEntry`](../../vasreadresult/readentry.md).

## See Also

### Getting customer information details
- [let barcodeMessage: String?](./barcodemessage.md)
  A message for the barcode.
- [let emailAddress: String?](./emailaddress.md)
  The customer’s email address or Hide My Email address if supported.
- [let phoneNumber: CNPhoneNumber?](./phonenumber.md)
  The customer’s phone number, if provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/customerinfo/customervasdata)*