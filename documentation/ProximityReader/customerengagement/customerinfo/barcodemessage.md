# barcodeMessage

**Framework**: ProximityReader  
**Kind**: property

A message for the barcode.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let barcodeMessage: String?
```

#### Discussion

The value is the `message` field of the barcode dictionary of the selected pass.

## See Also

- [let customerVASData: Data?](customerengagement/customerinfo/customervasdata.md)
  The encrypted VAS content of a selected Wallet pass.
- [let emailAddress: String?](customerengagement/customerinfo/emailaddress.md)
  The customer’s email address or Hide My Email address if supported.
- [let phoneNumber: CNPhoneNumber?](customerengagement/customerinfo/phonenumber.md)
  The customer’s phone number, if provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/customerinfo/barcodemessage)*