# RCSService.Business.CommunicationAddress

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing a business’ communication details.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct CommunicationAddress
```

## Topics

### Accessing communication details
- [let telephoneDetails: RCSService.Business.TelephoneDetails](./communicationaddress-swift.struct/telephonedetails.md)
  Telephone details for business.
- [RCSService.Business.TelephoneDetails](./telephonedetails.md)
  Structure containing the telephone number details provided by a business.
- [let uriEntries: [RCSService.Business.URIEntry]](./communicationaddress-swift.struct/urientries.md)
  URI entries provided by business.
- [RCSService.Business.URIEntry](./urientry.md)
  Structure containing details of a URI provided by a business.

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
- [RCSService.Business.VerificationDetails](./verificationdetails-swift.struct.md)
  Structure containing verification details of a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/communicationaddress-swift.struct)*