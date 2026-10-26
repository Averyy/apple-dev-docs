---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpostaladdress"
framework: "CareKit/CareKitStore"
---

# OCKPostalAddress

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A representation of the postal address for a contact.

## Declaration

```swift
struct OCKPostalAddress
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockpostaladdress/init%28from%29.md)
- [init(street: String, city: String, state: String, postalCode: String, country: String, isoCountryCode: String, subAdministrativeArea: String, subLocality: String)](./ockpostaladdress/init%28street,city,state,postalcode,country,isocountrycode,subadministrativearea,sublocality%29.md)
  A representation of the postal address for a contact.
### Instance Properties
- [var city: String](./ockpostaladdress/city.md)
  The city name of the address.
- [var country: String](./ockpostaladdress/country.md)
  The country or region name of the address.
- [var isoCountryCode: String](./ockpostaladdress/isocountrycode.md)
  The ISO country code, using the ISO 3166-1 alpha-2 standard.
- [var postalCode: String](./ockpostaladdress/postalcode.md)
  The postal code of the address.
- [var state: String](./ockpostaladdress/state.md)
  The state name of the address.
- [var street: String](./ockpostaladdress/street.md)
  The street name of the address.
- [var subAdministrativeArea: String](./ockpostaladdress/subadministrativearea.md)
  The subadministrative area (such as a county or other region) in a postal address.
- [var subLocality: String](./ockpostaladdress/sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.
### Instance Methods
- [func cnPostalAddress() -> CNPostalAddress](./ockpostaladdress/cnpostaladdress%28%29.md)
### Default Implementations
- [Equatable Implementations](./ockpostaladdress/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Contacts
- [struct OCKContact](./ockcontact.md)
  An `OCKContact` represents a contact that a user may want to get in touch with. A contact may be a care provider, a friend, or a family member. Contacts must have at least a name, and may optionally have numerous other addresses at which to be contacted.
- [protocol OCKAnyContact](./ockanycontact.md)
  Conforming a type to `OCKAnyContact` allows it to be queried and displayed by CareKit.
- [enum OCKBiologicalSex](./ockbiologicalsex.md)
  Represents a person’s biological sex.
- [enum OCKContactCategory](./ockcontactcategory.md)
  An enumerator specifying which group a contact belongs to.
- [struct OCKLabeledValue](./ocklabeledvalue.md)
  An optional label paired with a value used to represent contact information. The label will typically indicate what kind of information the value carries.
- [protocol OCKContactStore](./ockcontactstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyContact` is considered an `OCKCarePlanStore`.
- [protocol OCKAnyContactStore](./ockanycontactstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyContact` is considered an `OCKAnyContactStore`.
- [protocol OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
  A store that allows for reading contacts.
- [protocol OCKReadableContactStore](./ockreadablecontactstore.md)
  A store that allows for reading contacts.
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpostaladdress)*