# RCSService.Business.CommunicationAddress

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing a business’ communication details.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CommunicationAddress
```

## Topics

### Accessing communication details
- [let telephoneDetails: RCSService.Business.TelephoneDetails](rcsservice/business/communicationaddress-swift.struct/telephonedetails.md)
  Telephone details for business.
- [RCSService.Business.TelephoneDetails](rcsservice/business/telephonedetails.md)
  Structure containing the telephone number details provided by a business.
- [let uriEntries: [RCSService.Business.URIEntry]](rcsservice/business/communicationaddress-swift.struct/urientries.md)
  URI entries provided by business.
- [RCSService.Business.URIEntry](rcsservice/business/urientry.md)
  Structure containing details of a URI provided by a business.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/communicationaddress-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/communicationaddress-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing communication addresses
- [static func == (RCSService.Business.CommunicationAddress, RCSService.Business.CommunicationAddress) -> Bool](rcsservice/business/communicationaddress-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/communicationaddress-swift.struct/equatable-implementations.md)

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
- [RCSService.Business.VerificationDetails](rcsservice/business/verificationdetails-swift.struct.md)
  Structure containing verification details of a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/communicationaddress-swift.struct)*