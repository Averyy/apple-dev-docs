# CustomerEngagement.CustomerInfo

**Framework**: ProximityReader  
**Kind**: struct

A response structure that describes customer information.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct CustomerInfo
```

#### Overview

If none of the customer information is available, this structure can return with all the values being nil

## Topics

### Instance Properties
- [let barcodeMessage: String?](customerengagement/customerinfo/barcodemessage.md)
  A message for the barcode.
- [let customerVASData: Data?](customerengagement/customerinfo/customervasdata.md)
  The encrypted VAS content of a selected Wallet pass.
- [let emailAddress: String?](customerengagement/customerinfo/emailaddress.md)
  The customer’s email address or Hide My Email address if supported.
- [let phoneNumber: CNPhoneNumber?](customerengagement/customerinfo/phonenumber.md)
  The customer’s phone number, if provided.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/customerinfo)*