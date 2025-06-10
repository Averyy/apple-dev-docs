# NSTextContentType

**Framework**: AppKit  
**Kind**: struct

Constants that identify the semantic meaning for a text-entry area.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSTextContentType
```

#### Discussion

Use these constants with the [`contentType`](nstextcontent/contenttype.md) property.

## Topics

### Creating a content type
- [init(rawValue: String)](nstextcontenttype/init(rawvalue:).md)
  Creates a new content type with the raw value you provide.
### Defining web addresses
- [static let URL: NSTextContentType](nstextcontenttype/url.md)
  A property that defines the content in a text input area as a URL.
### Identifying contacts
- [static let namePrefix: NSTextContentType](nstextcontenttype/nameprefix.md)
  A property that defines the content in a text input area as a prefix or title, such as .
- [static let name: NSTextContentType](nstextcontenttype/name.md)
  A property that defines the content in a text input area as a name.
- [static let nameSuffix: NSTextContentType](nstextcontenttype/namesuffix.md)
  A property that defines the content in a text input area as a suffix, such as .
- [static let givenName: NSTextContentType](nstextcontenttype/givenname.md)
  A property that defines the content in a text input area as a first name.
- [static let middleName: NSTextContentType](nstextcontenttype/middlename.md)
  A property that defines the content in a text input area as a middle name.
- [static let familyName: NSTextContentType](nstextcontenttype/familyname.md)
  A property that defines the content in a text input area as a family name, or last name.
- [static let nickname: NSTextContentType](nstextcontenttype/nickname.md)
  A property that defines the content in a text input area as a nickname.
- [static let organizationName: NSTextContentType](nstextcontenttype/organizationname.md)
  A property that defines the content in a text input area as an organization name.
- [static let jobTitle: NSTextContentType](nstextcontenttype/jobtitle.md)
  A property that defines the content in a text input area as a job title.
### Setting location data
- [static let location: NSTextContentType](nstextcontenttype/location.md)
  A property that defines the content in a text input area as a location, such as a point of interest, an address, or another identifier for a location.
- [static let fullStreetAddress: NSTextContentType](nstextcontenttype/fullstreetaddress.md)
  A property that defines the content in a text input area as a street address that fully identifies a location.
- [static let streetAddressLine1: NSTextContentType](nstextcontenttype/streetaddressline1.md)
  A property that defines the content in a text input area as the first line of a street address.
- [static let streetAddressLine2: NSTextContentType](nstextcontenttype/streetaddressline2.md)
  A property that defines the content in a text input area as the second line of a street address.
- [static let addressCity: NSTextContentType](nstextcontenttype/addresscity.md)
  A property that defines the content in a text input area as a city name.
- [static let addressCityAndState: NSTextContentType](nstextcontenttype/addresscityandstate.md)
  A property that defines the content in a text input area as a city name with a state name.
- [static let addressState: NSTextContentType](nstextcontenttype/addressstate.md)
  A property that defines the content in a text input area as a state name.
- [static let postalCode: NSTextContentType](nstextcontenttype/postalcode.md)
  A property that defines the content in a text input area as a postal code.
- [static let sublocality: NSTextContentType](nstextcontenttype/sublocality.md)
  A property that defines the content in a text input area as a sublocality.
- [static let countryName: NSTextContentType](nstextcontenttype/countryname.md)
  A property that defines the content in a text input area as a country or region name.
### Managing accounts
- [static let username: NSTextContentType](nstextcontenttype/username.md)
  A property that defines the content in a text input area as an account or login name.
- [static let password: NSTextContentType](nstextcontenttype/password.md)
  A property that defines the content in a text input area as a password.
- [static let newPassword: NSTextContentType](nstextcontenttype/newpassword.md)
  A property that defines the content in a text input area as a new password.
### Securing accounts
- [static let oneTimeCode: NSTextContentType](nstextcontenttype/onetimecode.md)
  A property that defines the content in a text input area as a one-time code.
### Setting communication details
- [static let emailAddress: NSTextContentType](nstextcontenttype/emailaddress.md)
  A property that defines the content in a text input area as an email address.
- [static let telephoneNumber: NSTextContentType](nstextcontenttype/telephonenumber.md)
  A property that defines the content in a text input area as a telephone number.
### Accepting payment
- [static let creditCardNumber: NSTextContentType](nstextcontenttype/creditcardnumber.md)
  A property that defines the content in a text input area as a credit card number.
- [static let creditCardExpiration: NSTextContentType](nstextcontenttype/creditcardexpiration.md)
  A property that defines the content in a text input area as an expiration date on a credit card.
- [static let creditCardExpirationMonth: NSTextContentType](nstextcontenttype/creditcardexpirationmonth.md)
  A property that defines the content in a text input area as the month component of an expiration date on a credit card.
- [static let creditCardExpirationYear: NSTextContentType](nstextcontenttype/creditcardexpirationyear.md)
  A property that defines the content in a text input area as the year component of an expiration date on a credit card.
- [static let creditCardSecurityCode: NSTextContentType](nstextcontenttype/creditcardsecuritycode.md)
  A property that defines the content in a text input area as a credit card security code.
- [static let creditCardType: NSTextContentType](nstextcontenttype/creditcardtype.md)
  A property that defines the content in a text input area as a credit card type.
- [static let creditCardName: NSTextContentType](nstextcontenttype/creditcardname.md)
  A property that defines the content in a text input area as a name on a credit card.
- [static let creditCardGivenName: NSTextContentType](nstextcontenttype/creditcardgivenname.md)
  A property that defines the content in a text input area as a first name on a credit card.
- [static let creditCardMiddleName: NSTextContentType](nstextcontenttype/creditcardmiddlename.md)
  A property that defines the content in a text input area as a middle name on a credit card.
- [static let creditCardFamilyName: NSTextContentType](nstextcontenttype/creditcardfamilyname.md)
  A property that defines the content in a text input area as a family name, or last name, on a credit card.
### Getting birthday information
- [static let birthdate: NSTextContentType](nstextcontenttype/birthdate.md)
  A property that defines the content in a text input area as a date of birth.
- [static let birthdateDay: NSTextContentType](nstextcontenttype/birthdateday.md)
  A property that defines the content in a text input area as the day component of a birthdate.
- [static let birthdateMonth: NSTextContentType](nstextcontenttype/birthdatemonth.md)
  A property that defines the content in a text input area as the month component of a birthdate.
- [static let birthdateYear: NSTextContentType](nstextcontenttype/birthdateyear.md)
  A property that defines the content in a text input area as the year component of a birthdate.
### Scheduling events
- [static let dateTime: NSTextContentType](nstextcontenttype/datetime.md)
  A property that defines the content in a text input area as a date, time, or duration.
### Tracking events
- [static let flightNumber: NSTextContentType](nstextcontenttype/flightnumber.md)
  A property that defines the content in a text input area as an airline flight number.
- [static let shipmentTrackingNumber: NSTextContentType](nstextcontenttype/shipmenttrackingnumber.md)
  A property that defines the content in a text input area as a parcel tracking number.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var contentType: NSTextContentType?](nstextcontent/contenttype.md)
  The semantic meaning for a text input area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontenttype)*