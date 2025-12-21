# RCSService.Business.VerificationDetails

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing verification details of a business.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct VerificationDetails
```

## Topics

### Accessing verification properties
- [let isVerified: Bool](rcsservice/business/verificationdetails-swift.struct/isverified.md)
  Whether the business is verified.
- [let verifiedBy: String?](rcsservice/business/verificationdetails-swift.struct/verifiedby.md)
  Source of verification.
- [let expirationDate: Date?](rcsservice/business/verificationdetails-swift.struct/expirationdate.md)
  Expiration date of business information.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let communicationAddress: RCSService.Business.CommunicationAddress?](rcsservice/business/communicationaddress-swift.property.md)
  Communication details of business.
- [RCSService.Business.CommunicationAddress](rcsservice/business/communicationaddress-swift.struct.md)
  Structure containing a business’ communication details.
- [let addressEntries: [RCSService.Business.AddressEntry]](rcsservice/business/addressentries.md)
  Array of business’ address locations.
- [RCSService.Business.AddressEntry](rcsservice/business/addressentry.md)
  Structure containing address details provided by a business.
- [let emailAddress: String?](rcsservice/business/emailaddress.md)
  Service email address.
- [let websiteURL: URL?](rcsservice/business/websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](rcsservice/business/verificationdetails-swift.property.md)
  Verification information about business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/verificationdetails-swift.struct)*