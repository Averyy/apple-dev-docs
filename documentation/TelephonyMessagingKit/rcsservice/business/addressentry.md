# RCSService.Business.AddressEntry

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing address details provided by a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct AddressEntry
```

## Topics

### Accessing address details
- [let address: String](rcsservice/business/addressentry/address.md)
  Address of business.
- [let label: String](rcsservice/business/addressentry/label.md)
  Label for address.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let communicationAddress: RCSService.Business.CommunicationAddress?](rcsservice/business/communicationaddress-swift.property.md)
  Communication details of business.
- [RCSService.Business.CommunicationAddress](rcsservice/business/communicationaddress-swift.struct.md)
  Structure containing a business’ communication details.
- [let addressEntries: [RCSService.Business.AddressEntry]](rcsservice/business/addressentries.md)
  Array of business’ address locations.
- [let emailAddress: String?](rcsservice/business/emailaddress.md)
  Service email address.
- [let websiteURL: URL?](rcsservice/business/websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](rcsservice/business/verificationdetails-swift.property.md)
  Verification information about business.
- [RCSService.Business.VerificationDetails](rcsservice/business/verificationdetails-swift.struct.md)
  Structure containing verification details of a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/addressentry)*