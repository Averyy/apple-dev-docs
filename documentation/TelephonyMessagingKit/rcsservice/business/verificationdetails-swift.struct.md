# RCSService.Business.VerificationDetails

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing verification details of a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct VerificationDetails
```

## Topics

### Accessing verification properties
- [let isVerified: Bool](./verificationdetails-swift.struct/isverified.md)
  Whether the business is verified.
- [let verifiedBy: String?](./verificationdetails-swift.struct/verifiedby.md)
  Source of verification.
- [let expirationDate: Date?](./verificationdetails-swift.struct/expirationdate.md)
  Expiration date of business information.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing business contact information
- [let communicationAddress: RCSService.Business.CommunicationAddress?](./communicationaddress-swift.property.md)
  Communication details of business.
- [RCSService.Business.CommunicationAddress](./communicationaddress-swift.struct.md)
  Structure containing a business’ communication details.
- [let addressEntries: [RCSService.Business.AddressEntry]](./addressentries.md)
  Array of business’ address locations.
- [RCSService.Business.AddressEntry](./addressentry.md)
  Structure containing address details provided by a business.
- [let emailAddress: String?](./emailaddress.md)
  Service email address.
- [let websiteURL: URL?](./websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](./verificationdetails-swift.property.md)
  Verification information about business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/verificationdetails-swift.struct)*