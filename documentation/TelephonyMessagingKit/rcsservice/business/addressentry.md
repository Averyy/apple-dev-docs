# RCSService.Business.AddressEntry

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing address details provided by a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct AddressEntry
```

## Topics

### Accessing address details
- [let address: String](./addressentry/address.md)
  Address of business.
- [let label: String](./addressentry/label.md)
  Label for address.

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
- [let emailAddress: String?](./emailaddress.md)
  Service email address.
- [let websiteURL: URL?](./websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](./verificationdetails-swift.property.md)
  Verification information about business.
- [RCSService.Business.VerificationDetails](./verificationdetails-swift.struct.md)
  Structure containing verification details of a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/addressentry)*