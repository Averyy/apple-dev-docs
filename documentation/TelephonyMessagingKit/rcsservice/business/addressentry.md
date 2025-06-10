# RCSService.Business.AddressEntry

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing address details provided by a business.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/addressentry/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/addressentry/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing address entries
- [static func == (RCSService.Business.AddressEntry, RCSService.Business.AddressEntry) -> Bool](rcsservice/business/addressentry/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/addressentry/equatable-implementations.md)

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