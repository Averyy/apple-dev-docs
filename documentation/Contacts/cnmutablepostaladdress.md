# CNMutablePostalAddress

**Framework**: Contacts  
**Kind**: class

A mutable representation of the postal address for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNMutablePostalAddress
```

#### Overview

`CNMutablePostalAddress` is not a thread-safe class. To remove properties when saving a mutable postal address, set string properties to empty values.

## Topics

### Modifying the Parts of a Postal Address
- [var street: String](cnmutablepostaladdress/street.md)
  The street name of the address.
- [var city: String](cnmutablepostaladdress/city.md)
  The city name of the address.
- [var state: String](cnmutablepostaladdress/state.md)
  The state name of the address.
- [var postalCode: String](cnmutablepostaladdress/postalcode.md)
  The postal code of the address.
- [var country: String](cnmutablepostaladdress/country.md)
  The country or region name of the address.
- [var isoCountryCode: String](cnmutablepostaladdress/isocountrycode.md)
  The ISO country code, using the ISO 3166-1 alpha-2 standard.
- [var subAdministrativeArea: String](cnmutablepostaladdress/subadministrativearea.md)
  The subadministrative area (such as a county or other region) in a postal address.
- [var subLocality: String](cnmutablepostaladdress/sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.

## Relationships

### Inherits From
- [CNPostalAddress](cnpostaladdress.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CNPostalAddress](cnpostaladdress.md)
  An immutable representation of the postal address for a contact.
- [class CNInstantMessageAddress](cninstantmessageaddress.md)
  An immutable object representing an instant message address for the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablepostaladdress)*