# barcodeMessage

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

A message for the barcode.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
let barcodeMessage: String?
```

## Discussion

The value is the `message` field of the barcode dictionary of the selected pass.

## See Also

### Getting customer information details
- [let customerVASData: Data?](./customervasdata.md)
  The encrypted VAS content of a selected Wallet pass.
- [let emailAddress: String?](./emailaddress.md)
  The customer’s email address or Hide My Email address if supported.
- [let phoneNumber: CNPhoneNumber?](./phonenumber.md)
  The customer’s phone number, if provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/customerinfo/barcodemessage)*